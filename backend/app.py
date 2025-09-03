import base64
import io
import os
import cv2
import gc
import numpy as np
import uuid
import threading
import time
import queue
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image
import torch
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# AI Model Imports
try:
    from gfpgan import GFPGANer
    from realesrgan import RealESRGANer
    from basicsr.archs.rrdbnet_arch import RRDBNet
except ImportError as e:
    print(f"Could not import AI models: {e}")

# Initialize Flask app
app = Flask(__name__, static_folder='../', static_url_path='/')
CORS(app)

TASK_QUEUE = queue.Queue()
NUM_WORKERS = 2

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.lock = threading.Lock()

    def create_task(self, task_id, image_pixels=None):
        with self.lock:
            self.tasks[task_id] = {
                "status": "pending",
                "result": None,
                "cancelled": False,
                "created_at": time.time(),
                "image_size": image_pixels
            }

    def set_task_status(self, task_id, status):
        with self.lock:
            if task_id in self.tasks:
                self.tasks[task_id]["status"] = status
                return True
        return False

    def _calculate_timeout(self, image_pixels):
        if not image_pixels: 
            return 120
        megapixels = image_pixels / (1024 * 1024)
        if megapixels <= 2:
            return 30
        elif megapixels <= 8:
            return 120
        elif megapixels <= 20:
            return 300
        elif megapixels <= 50:
            return 600
        else:
            return 900

    def cancel_task(self, task_id):
        with self.lock:
            if task_id in self.tasks and self.tasks[task_id]["status"] in ["pending", "processing"]:
                self.tasks[task_id]["cancelled"] = True
                self.tasks[task_id]["status"] = "cancelled"
                return True
        return False

    def is_cancelled(self, task_id):
        with self.lock:
            return self.tasks.get(task_id, {}).get("cancelled", False)

    def complete_task(self, task_id, result):
        with self.lock:
            if task_id in self.tasks and not self.tasks[task_id]["cancelled"]:
                self.tasks[task_id]["status"] = "completed"
                self.tasks[task_id]["result"] = result

    def get_task_status(self, task_id):
        with self.lock:
            task = self.tasks.get(task_id, {})
            if task.get("status") == "pending":
                q_list = list(TASK_QUEUE.queue)
                for i, (tid, _) in enumerate(q_list):
                    if tid == task_id:
                        return {"status": "pending", "position": i + 1, "queue_size": len(q_list)}
                return {"status": "pending", "position": "N/A"}
            return {"status": task.get("status", "not_found")}

    def get_task_result(self, task_id):
        with self.lock:
            return self.tasks.get(task_id, {}).get("result")

    def cleanup_old_tasks(self):
        with self.lock:
            current_time = time.time()
            tasks_to_remove = []

            for task_id, task_info in self.tasks.items():
                task_age = current_time - task_info.get("created_at", current_time)

                if task_info["status"] == "processing" and task_age > self._calculate_timeout(task_info.get("image_size")):
                    self.cancel_task(task_id)

                if task_info["status"] in ["completed", "cancelled", "error"] and task_age > 180:
                    tasks_to_remove.append(task_id)

            if len(self.tasks) > 50:
                sorted_tasks = sorted(self.tasks.items(), key=lambda x: x[1].get("created_at", 0))
                tasks_to_remove.extend([task_id for task_id, _ in sorted_tasks[:len(self.tasks) - 50]])

            for task_id in set(tasks_to_remove):
                self.tasks.pop(task_id, None)

task_manager = TaskManager()

# Load AI Models
gfpganer = None
bg_upsampler = None

try:
    realesrgan_model_path = os.path.join('models', 'RealESRGAN_x4plus.pth')
    if os.path.exists(realesrgan_model_path):
        model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
        bg_upsampler = RealESRGANer(
            scale=4, model_path=realesrgan_model_path, model=model,
            tile=400, tile_pad=10, pre_pad=0, half=torch.cuda.is_available()
        )

    gfpgan_model_path = os.path.join('models', 'GFPGANv1.4.pth')
    if os.path.exists(gfpgan_model_path):
        gfpganer = GFPGANer(
            model_path=gfpgan_model_path, upscale=2, arch='clean',
            channel_multiplier=2, bg_upsampler=bg_upsampler
        )

    models_loaded = []
    if gfpganer:
        models_loaded.append("GFPGAN")
    if bg_upsampler:
        models_loaded.append("RealESRGAN")
    
    if models_loaded:
        print(f"Models loaded: {', '.join(models_loaded)}")

except Exception as e:
    print(f"Error loading models: {e}")

def pil_to_cv2(pil_image):
    return np.array(pil_image)[:, :, ::-1].copy()

def cv2_to_pil(cv2_image):
    return Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))

def process_image_task(task_id, task_info):
    try:
        if task_manager.is_cancelled(task_id):
            return

        if task_info["type"] == 'base64':
            header, encoded = task_info["data"].split(",", 1)
            binary_data = base64.b64decode(encoded)
        elif task_info["type"] == 'url':
            response = requests.get(task_info["data"], timeout=20, stream=True)
            response.raise_for_status()
            if not response.headers.get('content-type', '').startswith('image/'):
                raise ValueError("URL does not point to an image")
            binary_data = response.content
        else:
            raise ValueError(f"Unknown task type: {task_info['type']}")

        with Image.open(io.BytesIO(binary_data)) as temp_img:
            original_image_pil = temp_img.convert("RGB")
            original_image_cv2 = pil_to_cv2(original_image_pil)

        if task_manager.is_cancelled(task_id):
            return

        if gfpganer:
            _, _, repaired_image_cv2 = gfpganer.enhance(
                original_image_cv2, has_aligned=False,
                only_center_face=False, paste_back=True
            )
        else:
            raise Exception("GFPGAN model not available")

        if task_manager.is_cancelled(task_id):
            return

        repaired_image_pil = cv2_to_pil(repaired_image_cv2)
        buffered = io.BytesIO()
        repaired_image_pil.save(buffered, format="PNG", optimize=True, compress_level=6)
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        result = {'repairedImage': f"data:image/png;base64,{img_str}"}
        task_manager.complete_task(task_id, result)

        del original_image_cv2, repaired_image_cv2, repaired_image_pil, binary_data
        gc.collect()

    except Exception as e:
        task_manager.set_task_status(task_id, "error")
        task_manager.complete_task(task_id, {'error': str(e)})

def worker():
    while True:
        try:
            task_id, task_info = TASK_QUEUE.get(timeout=1)
            if not task_manager.is_cancelled(task_id):
                task_manager.set_task_status(task_id, "processing")
                process_image_task(task_id, task_info)
            TASK_QUEUE.task_done()
        except queue.Empty:
            continue

def periodic_cleanup():
    while True:
        time.sleep(30)
        task_manager.cleanup_old_tasks()
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route('/api/repair', methods=['POST'])
def handle_repair():
    if not gfpganer:
        return jsonify({'error': 'GFPGAN model not loaded'}), 500

    data = request.get_json()
    if not data or ('image' not in data and 'image_url' not in data):
        return jsonify({'error': 'No image data or image_url provided'}), 400

    task_id = str(uuid.uuid4())
    image_pixels = None

    if 'image' in data:
        try:
            header, encoded = data['image'].split(",", 1)
            binary_data = base64.b64decode(encoded)
            with Image.open(io.BytesIO(binary_data)) as temp_image:
                image_pixels = temp_image.width * temp_image.height
            task_info = {"type": "base64", "data": data['image']}
        except Exception as e:
            return jsonify({'error': f'Invalid image data: {str(e)}'}), 400
    else:
        image_url = data['image_url']
        if not isinstance(image_url, str) or not image_url.startswith(('http://', 'https://')):
             return jsonify({'error': 'Invalid URL format'}), 400
        task_info = {"type": "url", "data": image_url}

    task_manager.create_task(task_id, image_pixels)
    TASK_QUEUE.put((task_id, task_info))

    estimated_time = task_manager._calculate_timeout(image_pixels)
    megapixels = (image_pixels / (1024 * 1024)) if image_pixels else 'N/A'

    return jsonify({
        'task_id': task_id,
        'status': 'pending',
        'image_info': {
            'megapixels': round(megapixels, 1) if isinstance(megapixels, float) else megapixels,
            'estimated_time_seconds': estimated_time
        }
    })

@app.route('/api/status/<task_id>', methods=['GET'])
def get_status(task_id):
    response_data = task_manager.get_task_status(task_id)
    status = response_data.get("status")

    if status == "not_found":
        return jsonify({'error': 'Task not found'}), 404

    if status == "completed":
        result = task_manager.get_task_result(task_id)
        response_data['result'] = result
        if result and 'error' in result:
            return jsonify({'status': 'error', 'error': result['error']})

    return jsonify(response_data)

@app.route('/api/cancel/<task_id>', methods=['POST'])
def cancel_task_endpoint(task_id):
    if task_manager.cancel_task(task_id):
        return jsonify({'status': 'cancelled'})
    return jsonify({'status': 'cannot_cancel', 'message': 'Task already completed or not found'}), 404

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'models_loaded': {
            'gfpgan': gfpganer is not None,
            'realesrgan': bg_upsampler is not None
        },
        'workers': NUM_WORKERS,
        'tasks_in_queue': TASK_QUEUE.qsize(),
        'active_processing_tasks': len([t for t in task_manager.tasks.values() if t['status'] == 'processing']),
        'total_managed_tasks': len(task_manager.tasks),
        'cuda_available': torch.cuda.is_available()
    })

if __name__ == '__main__':
    for i in range(NUM_WORKERS):
        threading.Thread(target=worker, daemon=True, name=f"Worker-{i+1}").start()
    threading.Thread(target=periodic_cleanup, daemon=True, name="CleanupThread").start()
    app.run(host='0.0.0.0', port=5000, debug=False)