````markdown
# ImageRepair AI

<div align="center">
  <p>An intelligent AI tool to restore and enhance your photos, built with a robust backend to provide a smooth and transparent processing experience.</p>
</div>

<div align="center">

| Before (Original) | After (Restored) |
| :---: | :---: |
| <img src="./assets/before_real.jpg" width="400"> | <img src="./assets/after_real.jpg" width="400"> |
| <img src="./assets/before_anime.jpg" width="400"> | <img src="./assets/after_anime.jpg" width="400"> |

</div>

## Why is This Project Different?

While many AI tools exist, this project is engineered for a better user experience, giving you more insight and control over the image restoration process.

-   **Responsive Queuing System**: The backend is built to handle image processing in the background. This means that if you upload another image while one is already being processed, the application won't freeze or crash. Your new submission is simply added to a queue, and you can see its position and status, ensuring no work is lost.

-   **Real-Time Status Tracking**: Ever wondered how long an AI process will take? This tool provides a unique Task ID for every image you submit. The interface automatically updates to show you if your image is "pending" in the queue or actively "processing," giving you clear feedback on what's happening.

-   **Dual-AI Enhancement Pipeline**: To achieve the best results, the application combines the strengths of two powerful AI models. **GFPGAN** specializes in restoring faces with stunning realism, while **Real-ESRGAN** upscales and enhances the entire image background.

-   **User-Centric Interface**: The frontend is designed for a smooth workflow, featuring a multi-language interface, an interactive before/after comparison slider, and the ability to process images directly from a URL.

-   **Built for Easy Deployment**: With pre-configured Docker setups for both CPU and GPU, you can deploy this project on your own machine with a single command, confident that the environment is consistent and reliable.

## 🚀 Getting Started

The recommended way to run this project is with Docker, which handles all dependencies automatically.

### Prerequisites

-   [Git](https://git-scm.com/downloads)
-   [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)
-   **(For GPU acceleration)**: A compatible [NVIDIA GPU with drivers](https://www.nvidia.com/Download/index.aspx) and the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

### Installation & Launch with Docker

#### **CPU Version (works on any system)**

```bash
git clone [https://github.com/diandiancha/ImageRepair-AI.git](https://github.com/diandiancha/ImageRepair-AI.git)
````

```bash
cd ImageRepair-AI
```

```bash
docker-compose -f docker-compose.cpu.yml up --build
```

  - Access the web interface at: `http://localhost:5002`

#### **GPU Version (for high performance with an NVIDIA GPU)**

```bash
git clone [https://github.com/diandiancha/ImageRepair-AI.git](https://github.com/diandiancha/ImageRepair-AI.git)
```

```bash
cd ImageRepair-AI
```

```bash
docker-compose -f docker-compose.gpu.yml up --build
```

  - Access the web interface at: `http://localhost:5001`

-----

\<details\>
\<summary\>💻 **For Developers: Manual Python Virtual Environment Setup**\</summary\>

This method is for users who want to run the application outside of Docker.

#### **Step 1: Clone Repository**

```bash
git clone [https://github.com/diandiancha/ImageRepair-AI.git](https://github.com/diandiancha/ImageRepair-AI.git)
```

```bash
cd ImageRepair-AI
```

#### **Step 2: Create and Activate Virtual Environment**

```bash
python -m venv venv
```

  - On Windows:

<!-- end list -->

```bash
venv\Scripts\activate
```

  - On macOS/Linux:

<!-- end list -->

```bash
source venv/bin/activate
```

#### **Step 3: Install Dependencies**

  - **For CPU-only:**

    ```bash
    pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu)
    ```

    ```bash
    pip install -r backend/requirements.txt
    ```

  - **For GPU-acceleration (NVIDIA CUDA required):**

    ```bash
    pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2 --extra-index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)
    ```

    ```bash
    pip install -r backend/requirements.txt
    ```

#### **Step 4: Download AI Models**

```bash
mkdir backend/models
```

```bash
wget -O backend/models/GFPGANv1.4.pth [https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth](https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth)
```

```bash
wget -O backend/models/RealESRGAN_x4plus.pth [https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth)
```

#### **Step 5: Run the Application**

```bash
python backend/app.py
```

  - The application will be available at `http://localhost:5000`.

\</details\>

\<br\>

\<details\>
\<summary\>🛠️ **Technical Details (API, Configuration, etc.)**\</summary\>

#### Project Structure

```
ImageRepair-AI/
├── backend/
│   ├── app.py                 # Flask backend with task queue
│   ├── Dockerfile.cpu         # CPU Docker image definition
│   ├── Dockerfile.gpu         # GPU Docker image definition
│   └── requirements.txt       # Python dependencies
├── assets/
│   └── (comparison images)
├── .gitignore                 # Specifies files for Git to ignore
├── docker-compose.cpu.yml     # Docker Compose for CPU
├── docker-compose.gpu.yml     # Docker Compose for GPU
├── index.html                 # Frontend single-page application
└── README.md                  # This file
```

#### API Endpoints

All endpoints are defined in `backend/app.py`.

| Endpoint | Method | Description |
|---|---|---|
| `/api/repair` | `POST` | Submits an image for restoration. |
| `/api/status/<task_id>`| `GET` | Checks the status of a submitted task. |
| `/api/cancel/<task_id>`| `POST` | Requests to cancel a task. |
| `/api/health` | `GET` | Provides a health check of the service. |

\</details\>

## 🙏 Acknowledgments

This project stands on the shoulders of giants. My heartfelt thanks go to the creators of these incredible open-source models:

  - [GFPGAN](https://github.com/TencentARC/GFPGAN)
  - [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
  - [BasicSR](https://github.com/XPixelGroup/BasicSR)

<!-- end list -->

```
```
