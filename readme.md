# ImageRepair AI

[English](#english) | [中文简体](#中文简体) | [繁體中文](#繁體中文) | [日本語](#日本語) | [한국어](#한국어)

---

## English

### 🎯 Overview

ImageRepair AI is a powerful, free, and open-source web application that uses advanced AI models to restore, enhance, and repair damaged images. Built with GFPGAN and RealESRGAN, it can fix scratches, reduce blur, enhance details, and upscale images with remarkable quality.

**Key Features:**
- 🤖 AI-powered image restoration using GFPGAN
- 📈 Image upscaling with RealESRGAN (4x resolution enhancement)
- 🌐 Modern web interface with drag-and-drop support
- 🔒 Privacy-focused (images are not stored on servers)
- ⚡ GPU acceleration support
- 🌍 Multi-language support (EN/ZH/JA/KO)
- 🐳 Docker deployment ready

### 📋 System Requirements

#### Minimum Requirements
- **CPU**: Multi-core processor (Intel i5 or AMD Ryzen 5 equivalent)
- **RAM**: 8GB (16GB recommended for large images)
- **Storage**: 5GB free space for models and dependencies
- **Python**: 3.8 or higher
- **OS**: Windows 10+, macOS 10.14+, or Linux Ubuntu 18.04+

#### GPU Requirements (Optional but Recommended)
- **NVIDIA GPU**: GTX 1060 6GB or better
- **VRAM**: 6GB+ for optimal performance
- **CUDA**: Compatible GPU with CUDA 11.8+ support

### 🚀 Quick Start

#### Method 1: Docker Deployment (Recommended)

**For CPU-only systems:**
```bash
# Clone the repository
git clone <your-repo-url>
cd image-repair-ai

# Build and run CPU version
docker-compose -f docker-compose.cpu.yml up --build
```

**For GPU-enabled systems:**
```bash
# Clone the repository
git clone <your-repo-url>
cd image-repair-ai

# Build and run GPU version
docker-compose -f docker-compose.gpu.yml up --build
```

Access the application at `http://localhost:5002` (CPU) or `http://localhost:5001` (GPU).

#### Method 2: Python Virtual Environment

**Step 1: Setup Environment**
```bash
# Clone repository
git clone <your-repo-url>
cd image-repair-ai

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**Step 2: Install Dependencies**

For CPU-only installation:
```bash
pip install -r requirements.txt
```

For GPU-accelerated installation (NVIDIA CUDA required):
```bash
# Install GPU version of PyTorch first
pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2 --extra-index-url https://download.pytorch.org/whl/cu121

# Then install other requirements
pip install -r requirements.txt
```

**Step 3: Download AI Models**
```bash
# Create models directory
mkdir models

# Download GFPGAN model (required)
wget -O models/GFPGANv1.4.pth https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth

# Download RealESRGAN model (required)
wget -O models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```

**Step 4: Run Application**
```bash
python app.py
```

Access the application at `http://localhost:5000`.

### 📁 Project Structure

```
image-repair-ai/
├── app.py                     # Flask backend application
├── index.html                 # Frontend web interface
├── requirements.txt           # Python dependencies
├── docker-compose.cpu.yml     # Docker config for CPU
├── docker-compose.gpu.yml     # Docker config for GPU
├── backend/
│   ├── Dockerfile.cpu         # CPU Docker image
│   └── Dockerfile.gpu         # GPU Docker image
├── models/                    # AI model files (download required)
│   ├── GFPGANv1.4.pth        # Face enhancement model
│   └── RealESRGAN_x4plus.pth # Upscaling model
└── README.md                  # This file
```

### 🔧 Configuration

#### Environment Variables
- `FLASK_ENV`: Set to `production` for production deployment
- `WORKERS`: Number of processing workers (default: 2)

#### Model Configuration
The application automatically detects and loads available models:
- **GFPGAN**: Face restoration and enhancement
- **RealESRGAN**: General image upscaling and enhancement

### 📊 API Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/api/repair` | POST | Start image repair task |
| `/api/status/<task_id>` | GET | Check task status |
| `/api/cancel/<task_id>` | POST | Cancel processing task |
| `/api/health` | GET | System health check |

### 🐳 Docker Deployment Details

#### CPU Version (`docker-compose.cpu.yml`)
- Port: 5002
- Optimized for systems without dedicated GPU
- Lower memory requirements

#### GPU Version (`docker-compose.gpu.yml`)
- Port: 5001
- Requires NVIDIA Docker runtime
- GPU acceleration enabled
- Higher performance for large images

### 🔍 Troubleshooting

#### Common Issues

**Model Loading Errors:**
```bash
# Ensure models are downloaded
ls -la models/
# Should show GFPGANv1.4.pth and RealESRGAN_x4plus.pth
```

**CUDA Out of Memory:**
- Reduce image size before processing
- Use CPU version for very large images
- Adjust tile size in model configuration

**Docker GPU Issues:**
```bash
# Verify NVIDIA Docker support
nvidia-docker --version
nvidia-smi
```

### 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### 📄 License

This project is open-source and available under the MIT License.

### 🙏 Acknowledgments

- [GFPGAN](https://github.com/TencentARC/GFPGAN) - Face restoration model
- [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) - Image super-resolution model
- [BasicSR](https://github.com/XPixelGroup/BasicSR) - Image restoration toolkit

---

## 中文简体

### 🎯 项目概述

ImageRepair AI 是一个强大、免费且开源的网络应用程序，使用先进的 AI 模型来修复、增强和修复损坏的图像。基于 GFPGAN 和 RealESRGAN 构建，可以修复划痕、减少模糊、增强细节并以卓越的质量放大图像。

**主要特性:**
- 🤖 使用 GFPGAN 进行 AI 图像修复
- 📈 使用 RealESRGAN 进行图像放大（4倍分辨率增强）
- 🌐 支持拖放的现代网页界面
- 🔒 注重隐私（图像不存储在服务器上）
- ⚡ 支持 GPU 加速
- 🌍 多语言支持（中英日韩）
- 🐳 支持 Docker 部署

### 📋 系统要求

#### 最低要求
- **CPU**: 多核处理器（Intel i5 或 AMD Ryzen 5 同等级别）
- **内存**: 8GB（推荐16GB用于大图像）
- **存储**: 5GB 空闲空间用于模型和依赖
- **Python**: 3.8 或更高版本
- **操作系统**: Windows 10+, macOS 10.14+, 或 Linux Ubuntu 18.04+

#### GPU 要求（可选但推荐）
- **NVIDIA GPU**: GTX 1060 6GB 或更好
- **显存**: 6GB+ 以获得最佳性能
- **CUDA**: 支持 CUDA 11.8+ 的兼容 GPU

### 🚀 快速开始

#### 方法1: Docker 部署（推荐）

**仅CPU系统:**
```bash
# 克隆仓库
git clone <your-repo-url>
cd image-repair-ai

# 构建并运行CPU版本
docker-compose -f docker-compose.cpu.yml up --build
```

**GPU支持系统:**
```bash
# 克隆仓库
git clone <your-repo-url>
cd image-repair-ai

# 构建并运行GPU版本
docker-compose -f docker-compose.gpu.yml up --build
```

在 `http://localhost:5002`（CPU）或 `http://localhost:5001`（GPU）访问应用程序。

#### 方法2: Python虚拟环境

**步骤1: 设置环境**
```bash
# 克隆仓库
git clone <your-repo-url>
cd image-repair-ai

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**步骤2: 安装依赖**

仅CPU安装:
```bash
pip install -r requirements.txt
```

GPU加速安装（需要NVIDIA CUDA）:
```bash
# 先安装GPU版本的PyTorch
pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2 --extra-index-url https://download.pytorch.org/whl/cu121

# 然后安装其他要求
pip install -r requirements.txt
```

**步骤3: 下载AI模型**
```bash
# 创建models目录
mkdir models

# 下载GFPGAN模型（必需）
wget -O models/GFPGANv1.4.pth https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth

# 下载RealESRGAN模型（必需）
wget -O models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```

**步骤4: 运行应用**
```bash
python app.py
```

在 `http://localhost:5000` 访问应用程序。

---

## 繁體中文

### 🎯 專案概述

ImageRepair AI 是一個強大、免費且開源的網路應用程式，使用先進的 AI 模型來修復、增強和修復損壞的圖像。基於 GFPGAN 和 RealESRGAN 構建，可以修復刮痕、減少模糊、增強細節並以卓越的品質放大圖像。

**主要特性:**
- 🤖 使用 GFPGAN 進行 AI 圖像修復
- 📈 使用 RealESRGAN 進行圖像放大（4倍解析度增強）
- 🌐 支援拖放的現代網頁介面
- 🔒 注重隱私（圖像不儲存在伺服器上）
- ⚡ 支援 GPU 加速
- 🌍 多語言支援（中英日韓）
- 🐳 支援 Docker 部署

### 📋 系統要求

#### 最低要求
- **CPU**: 多核心處理器（Intel i5 或 AMD Ryzen 5 同等級別）
- **記憶體**: 8GB（推薦16GB用於大圖像）
- **儲存**: 5GB 可用空間用於模型和相依性
- **Python**: 3.8 或更高版本
- **作業系統**: Windows 10+, macOS 10.14+, 或 Linux Ubuntu 18.04+

#### GPU 要求（可選但推薦）
- **NVIDIA GPU**: GTX 1060 6GB 或更好
- **顯示記憶體**: 6GB+ 以獲得最佳效能
- **CUDA**: 支援 CUDA 11.8+ 的相容 GPU

### 🚀 快速開始

#### 方法1: Docker 部署（推薦）

**僅CPU系統:**
```bash
# 複製儲存庫
git clone <your-repo-url>
cd image-repair-ai

# 構建並運行CPU版本
docker-compose -f docker-compose.cpu.yml up --build
```

**GPU支援系統:**
```bash
# 複製儲存庫
git clone <your-repo-url>
cd image-repair-ai

# 構建並運行GPU版本
docker-compose -f docker-compose.gpu.yml up --build
```

在 `http://localhost:5002`（CPU）或 `http://localhost:5001`（GPU）存取應用程式。

#### 方法2: Python虛擬環境

**步驟1: 設置環境**
```bash
# 複製儲存庫
git clone <your-repo-url>
cd image-repair-ai

# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**步驟2: 安裝相依性**

僅CPU安裝:
```bash
pip install -r requirements.txt
```

GPU加速安裝（需要NVIDIA CUDA）:
```bash
# 先安裝GPU版本的PyTorch
pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2 --extra-index-url https://download.pytorch.org/whl/cu121

# 然後安裝其他要求
pip install -r requirements.txt
```

**步驟3: 下載AI模型**
```bash
# 建立models目錄
mkdir models

# 下載GFPGAN模型（必需）
wget -O models/GFPGANv1.4.pth https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth

# 下載RealESRGAN模型（必需）
wget -O models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```

**步驟4: 執行應用程式**
```bash
python app.py
```

在 `http://localhost:5000` 存取應用程式。

---

## 日本語

### 🎯 プロジェクト概要

ImageRepair AI は、先進的なAIモデルを使用して画像を復元、強化、修復する強力で無料のオープンソースWebアプリケーションです。GFPGAN と RealESRGAN をベースに構築されており、傷の修復、ぼかしの軽減、詳細の強化、そして驚くべき品質での画像のアップスケールが可能です。

**主な機能:**
- 🤖 GFPGAN を使用したAI画像復元
- 📈 RealESRGAN による画像アップスケール（4倍解像度向上）
- 🌐 ドラッグ&ドロップ対応のモダンなWebインターフェース
- 🔒 プライバシー重視（画像はサーバーに保存されません）
- ⚡ GPU アクセラレーション対応
- 🌍 多言語サポート（英中日韓）
- 🐳 Docker デプロイメント対応

### 📋 システム要件

#### 最小要件
- **CPU**: マルチコアプロセッサ（Intel i5 または AMD Ryzen 5 同等）
- **メモリ**: 8GB（大きな画像には16GB推奨）
- **ストレージ**: モデルと依存関係用に5GBの空き容量
- **Python**: 3.8以上
- **OS**: Windows 10+, macOS 10.14+, または Linux Ubuntu 18.04+

#### GPU要件（オプションだが推奨）
- **NVIDIA GPU**: GTX 1060 6GB以上
- **VRAM**: 最適なパフォーマンスのために6GB+
- **CUDA**: CUDA 11.8+対応の互換GPU

### 🚀 クイックスタート

#### 方法1: Docker デプロイメント（推奨）

**CPUのみのシステム:**
```bash
# リポジトリをクローン
git clone <your-repo-url>
cd image-repair-ai

# CPU版をビルドして実行
docker-compose -f docker-compose.cpu.yml up --build
```

**GPU対応システム:**
```bash
# リポジトリをクローン
git clone <your-repo-url>
cd image-repair-ai

# GPU版をビルドして実行
docker-compose -f docker-compose.gpu.yml up --build
```

`http://localhost:5002`（CPU）または `http://localhost:5001`（GPU）でアプリケーションにアクセスします。

#### 方法2: Python仮想環境

**ステップ1: 環境セットアップ**
```bash
# リポジトリをクローン
git clone <your-repo-url>
cd image-repair-ai

# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**ステップ2: 依存関係のインストール**

CPUのみのインストール:
```bash
pip install -r requirements.txt
```

GPU加速インストール（NVIDIA CUDA必須）:
```bash
# 最初にGPU版PyTorchをインストール
pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2 --extra-index-url https://download.pytorch.org/whl/cu121

# その後、他の要件をインストール
pip install -r requirements.txt
```

**ステップ3: AIモデルのダウンロード**
```bash
# modelsディレクトリを作成
mkdir models

# GFPGANモデルをダウンロード（必須）
wget -O models/GFPGANv1.4.pth https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth

# RealESRGANモデルをダウンロード（必須）
wget -O models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```

**ステップ4: アプリケーションの実行**
```bash
python app.py
```

`http://localhost:5000` でアプリケーションにアクセスします。

---

## 한국어

### 🎯 프로젝트 개요

ImageRepair AI는 고급 AI 모델을 사용하여 이미지를 복원, 향상 및 수리하는 강력하고 무료이며 오픈소스인 웹 애플리케이션입니다. GFPGAN과 RealESRGAN을 기반으로 구축되어 긁힌 자국을 수정하고, 흐림을 줄이며, 세부사항을 향상시키고, 놀라운 품질로 이미지를 업스케일할 수 있습니다.

**주요 기능:**
- 🤖 GFPGAN을 사용한 AI 이미지 복원
- 📈 RealESRGAN을 통한 이미지 업스케일링 (4배 해상도 향상)
- 🌐 드래그 앤 드롭을 지원하는 현대적인 웹 인터페이스
- 🔒 개인정보 보호 중심 (이미지는 서버에 저장되지 않음)
- ⚡ GPU 가속 지원
- 🌍 다국어 지원 (영중일한)
- 🐳 Docker 배포 지원

### 📋 시스템 요구사항

#### 최소 요구사항
- **CPU**: 멀티코어 프로세서 (Intel i5 또는 AMD Ryzen 5 동급)
- **RAM**: 8GB (대용량 이미지의 경우 16GB 권장)
- **저장공간**: 모델 및 의존성을 위한 5GB 여유 공간
- **Python**: 3.8 이상
- **OS**: Windows 10+, macOS 10.14+, 또는 Linux Ubuntu 18.04+

#### GPU 요구사항 (선택사항이지만 권장)
- **NVIDIA GPU**: GTX 1060 6GB 이상
- **VRAM**: 최적 성능을 위해 6GB+
- **CUDA**: CUDA 11.8+ 지원 호환 GPU

### 🚀 빠른 시작

#### 방법 1: Docker 배포 (권장)

**CPU 전용 시스템:**
```bash
# 저장소 복제
git clone <your-repo-url>
cd image-repair-ai

# CPU 버전 빌드 및 실행
docker-compose -f docker-compose.cpu.yml up --build
```

**GPU 지원 시스템:**
```bash
# 저장소 복제
git clone <your-repo-url>
cd image-repair-ai

# GPU 버전 빌드 및 실행
docker-compose -f docker-compose.gpu.yml up --build
```

`http://localhost:5002` (CPU) 또는 `http://localhost:5001` (GPU)에서 애플리케이션에 접근합니다.

#### 방법 2: Python 가상환경

**1단계: 환경 설정**
```bash
# 저장소 복제
git clone <your-repo-url>
cd image-repair-ai

# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**2단계: 의존성 설치**

CPU 전용 설치:
```bash
pip install -r requirements.txt
```

GPU 가속 설치 (NVIDIA CUDA 필요):
```bash
# 먼저 GPU 버전 PyTorch 설치
pip install torch==2.1.2+cu121 torchvision==0.16.2+cu121 torchaudio==2.1.2 --extra-index-url https://download.pytorch.org/whl/cu121

# 그 다음 다른 요구사항 설치
pip install -r requirements.txt
```

**3단계: AI 모델 다운로드**
```bash
# models 디렉토리 생성
mkdir models

# GFPGAN 모델 다운로드 (필수)
wget -O models/GFPGANv1.4.pth https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth

# RealESRGAN 모델 다운로드 (필수)
wget -O models/RealESRGAN_x4plus.pth https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```

**4단계: 애플리케이션 실행**
```bash
python app.py
```

`http://localhost:5000`에서 애플리케이션에 접근합니다.

---

### 📸 Before/After Comparison

![Image Repair Comparison](comparison-placeholder.jpg)
*Left: Original damaged image | Right: AI-repaired result*

---

### 📞 Support

For issues, questions, or contributions, please visit our GitHub repository or create an issue.

**Made with ❤️ by the open-source community**