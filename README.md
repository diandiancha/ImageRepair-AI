# ImageRepair AI

<div align="center">
  <p>An intelligent, self-hostable AI tool to restore and enhance your photos, built with a robust backend for a smooth and transparent processing experience.</p>
</div>

<div align="center">

| Before (Original)                                   | After (Restored)                                  |
| :--------------------------------------------------: | :-------------------------------------------------: |
| <img src="./assets/before_real.jpg" width="400">     | <img src="./assets/after_real.jpg" width="400">     |
| <img src="./assets/before_anime.jpg" width="400">   | <img src="./assets/after_anime.jpg" width="400">   |

</div>

## ✨ Key Features

This project is engineered for a superior user experience, giving you more insight and control over the image restoration process.

-   **Asynchronous Task Queue**: The backend uses a worker and queue system to process images in the background. Tasks are queued and processed sequentially with real-time status updates.
-   **Real-Time Status Tracking**: Each submission receives a unique Task ID. The interface automatically polls the backend to show if your image is `pending` (with its queue position) or actively `processing`, providing clear, real-time feedback.
-   **Dual-AI Enhancement Pipeline**: Combines the strengths of two powerful AI models: **GFPGAN** specializes in restoring faces with stunning realism, while **Real-ESRGAN** upscales and enhances the entire image, including backgrounds.
-   **User-Centric Interface**: A clean and modern UI featuring drag-and-drop, direct URL processing, an interactive before/after comparison slider, and multi-language support (English, 简体中文, 繁體中文, 日本語, 한국어).
-   **Containerized for Easy Deployment**: Includes pre-configured Docker and Docker Compose files for both **CPU** and **GPU** environments, ensuring a consistent and reliable setup with a single command.

## 🚀 Getting Started

The recommended way to run this project is with Docker, which handles all dependencies and configuration automatically.

### Prerequisites

-   [Git](https://git-scm.com/downloads)
-   [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)
-   **(For GPU acceleration)**: A compatible [NVIDIA GPU with drivers](https://www.nvidia.com/Download/index.aspx) and the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

### Installation & Launch with Docker

#### **CPU Version (works on any system)**

```bash
git clone https://github.com/diandiancha/ImageRepair-AI.git
cd ImageRepair-AI
docker-compose -f docker-compose.cpu.yml up --build
```

Access the web interface at: `http://localhost:5002`

-----

#### **GPU Version (for high performance with an NVIDIA GPU)**

```bash
git clone https://github.com/diandiancha/ImageRepair-AI.git
cd ImageRepair-AI
docker-compose -f docker-compose.gpu.yml up --build
```

Access the web interface at: `http://localhost:5001`

#### **GPU Minimum Requirements**
- **NVIDIA GPU**: GTX 1060 6GB or better
- **VRAM**: 6GB+ for optimal performance
- **CUDA**: Compatible GPU with CUDA 11.8+ support
- **RAM**: 8GB system memory (16GB recommended for large images)
- **Storage**: 5GB free space for models and dependencies

<br>
<details>
<summary>🛠️ Technical Details</summary>

### Project Structure

```
ImageRepair-AI/
├── backend/
│   ├── app.py                 # Flask backend with task queue and API
│   ├── Dockerfile.cpu         # Docker build definition for CPU
│   ├── Dockerfile.gpu         # Docker build definition for GPU
│   └── requirements.txt       # Python dependencies
├── assets/
│   └── (comparison images)
├── .gitignore
├── docker-compose.cpu.yml     # Docker Compose configuration for CPU
├── docker-compose.gpu.yml     # Docker Compose configuration for GPU
├── index.html                 # Single-page frontend application
└── README.md
```

### API Endpoints

All endpoints are defined in `backend/app.py`.

| Endpoint               | Method | Description                                                              |
| ---------------------- | ------ | ------------------------------------------------------------------------ |
| `/api/repair`          | `POST` | Submits an image (base64 or URL) for restoration. Returns a `task_id`.     |
| `/api/status/<task_id>`| `GET`  | Checks the status of a submitted task (`pending`, `processing`, `completed`). |
| `/api/cancel/<task_id>`| `POST` | Requests to cancel a pending or processing task.                         |
| `/api/health`          | `GET`  | Provides a health check of the service, including model status and queue size. |

<br>
<details>
<summary>💻 Manual Python Virtual Environment Setup</summary>

This method is for developers who want to run the application outside of Docker.

**Step 1: Clone Repository**

```bash
git clone https://github.com/diandiancha/ImageRepair-AI.git
cd ImageRepair-AI
```

**Step 2: Create and Activate Virtual Environment**

```bash
python -m venv venv
```

*On Windows:*

```bash
venv\Scripts\activate
```

*On macOS/Linux:*

```bash
source venv/bin/activate
```

**Step 3: Install Dependencies**

*For CPU-only:*

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r backend/requirements.txt
```

*For GPU-acceleration (NVIDIA CUDA 12.1 required):*

```bash
pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2+cu121 --extra-index-url https://download.pytorch.org/whl/cu121
pip install -r backend/requirements.txt
```

**Step 4: Download AI Models**

```bash
mkdir backend/models
wget -O backend/models/GFPGANv1.4.pth https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth
wget -O backend/models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```

**Step 5: Run the Application**

```bash
# From the root "ImageRepair-AI" directory
python backend/app.py
```

The application will be available at `http://localhost:5000`.

</details>
</details>

## 🙏 Acknowledgments

This project stands on the shoulders of giants. Our heartfelt thanks go to the creators of these incredible open-source models:

  - [**GFPGAN**](https://github.com/TencentARC/GFPGAN)
  - [**Real-ESRGAN**](https://github.com/xinntao/Real-ESRGAN)
  - [**BasicSR**](https://github.com/xinntao/BasicSR)
