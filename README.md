# ImageRepair AI

<div align="center">
  <p>An intelligent, production-ready AI tool to restore and enhance your photos with real-time feedback.</p>
</div>

<div align="center">

| Before (Original) | After (Restored) |
| :---: | :---: |
| <img src="./assets/before_real.jpg" width="400"> | <img src="./assets/after_real.jpg" width="400"> |
| <img src="./assets/before_anime.jpg" width="400"> | <img src="./assets/after_anime.jpg" width="400"> |

</div>

## Why is This Project Different?

Ever used an online AI tool and been left staring at a spinning loader with no idea what's happening? ImageRepair AI is engineered to be different. It's not just a script, but a robust service designed for a transparent and interactive user experience.

-   **Robust Queuing System**: We use an asynchronous, multi-worker backend. If multiple users submit images, the system queues them fairly and processes them efficiently without freezing. You'll even know your position in the queue.

-   **Real-Time Status & Control**: Every job you submit gets a unique Task ID. Use our API to get live updates on your image's status—from "pending" to "processing" to "completed". If you change your mind, you can even request to cancel an ongoing task.

-   **Dual-AI Enhancement Pipeline**: We combine the strengths of two powerful AI models. **GFPGAN** focuses on restoring faces with stunning realism, while **Real-ESRGAN** upscales and enhances the entire image background. The result is a comprehensively repaired photo.

-   **User-Centric Interface**: The frontend is designed for a smooth workflow, featuring a multi-language interface, an interactive before/after comparison slider, and the ability to process images directly from a URL.

-   **Built for Deployment**: With pre-configured Docker setups for both CPU and GPU, you can deploy this project with a single command, confident that the environment is consistent and reliable.

## 🚀 Getting Started

The recommended way to run this project is with Docker, which handles all dependencies automatically.

### Prerequisites

-   [Git](https://git-scm.com/downloads)
-   [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)
-   **(For GPU acceleration)**: A compatible [NVIDIA GPU with drivers](https://www.nvidia.com/Download/index.aspx) and the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

### Installation & Launch

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/diandiancha/ImageRepair-AI.git
    cd ImageRepair-AI
    ```

2.  **Launch with Docker Compose:**

    -   **For CPU Version** (works on any system):
        ```bash
        docker-compose -f docker-compose.cpu.yml up --build
        ```
        - Access the web interface at: `http://localhost:5002`

    -   **For GPU Version** (for high performance with an NVIDIA GPU):
        ```bash
        docker-compose -f docker-compose.gpu.yml up --build
        ```
        - Access the web interface at: `http://localhost:5001`

The `--build` flag is only necessary for the first launch.

---

<details>
<summary>💻 For Developers: Manual Python Virtual Environment Setup</summary>

This method is for users who want to run the application outside of Docker.

1.  **Create and Activate Virtual Environment**
    ```bash
    # From the project's root directory
    python -m venv venv
    
    # On Windows:
    venv\Scripts\activate
    
    # On macOS/Linux:
    source venv/bin/activate
    ```

2.  **Install Dependencies**
    The dependencies are listed in `backend/requirements.txt`.

    -   **For CPU-only:**
        ```bash
        pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
        pip install -r backend/requirements.txt
        ```

    -   **For GPU-acceleration (NVIDIA CUDA required):**
        ```bash
        pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2 --extra-index-url https://download.pytorch.org/whl/cu121
        pip install -r backend/requirements.txt
        ```

3.  **Download AI Models**
    The Docker build process does this automatically, but for a manual setup, you must download the models yourself.
    ```bash
    # Create the directory
    mkdir backend/models

    # Download models into the new directory
    wget -O backend/models/GFPGANv1.4.pth https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth
    wget -O backend/models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
    ```

4.  **Run the Application**
    ```bash
    python backend/app.py
    ```
    - The application will be available at `http://localhost:5000`.

</details>

<br>

<details>
<summary>🛠️ Technical Details (API, Configuration, etc.)</summary>

#### Project Structure

```
ImageRepair-AI/
├── backend/
│   ├── app.py                 \# Flask backend with task queue
│   ├── Dockerfile.cpu         \# CPU Docker image definition
│   ├── Dockerfile.gpu         \# GPU Docker image definition
│   └── requirements.txt       \# Python dependencies
├── assets/
│   └── (comparison images)
├── .gitignore                 \# Specifies files for Git to ignore
├── docker-compose.cpu.yml     \# Docker Compose for CPU
├── docker-compose.gpu.yml     \# Docker Compose for GPU
├── index.html                 \# Frontend single-page application
└── README.md                  \# This file
```
#### API Endpoints
All endpoints are defined in `backend/app.py`.

| Endpoint | Method | Description |
|---|---|---|
| `/api/repair` | `POST` | Submits an image for restoration. |
| `/api/status/<task_id>`| `GET` | Checks the status of a submitted task. |
| `/api/cancel/<task_id>`| `POST` | Requests to cancel a task. |
| `/api/health` | `GET` | Provides a health check of the service. |

</details>

## 🙏 Acknowledgments

This project stands on the shoulders of giants. Our heartfelt thanks go to the creators of these incredible open-source models:
-   [GFPGAN](https://github.com/TencentARC/GFPGAN)
-   [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
-   [BasicSR](https://github.com/XPixelGroup/BasicSR)
```
