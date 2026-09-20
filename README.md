# 🛋️ Hệ Thống Phân Loại Sản Phẩm Nội Thất & Trực Quan Hóa Grad-CAM

> **Đề tài Thực tập Tốt nghiệp:** Nghiên cứu, ứng dụng Mạng nơ-ron Tích chập (CNN) và Kỹ thuật trực quan hóa Grad-CAM trong bài toán Phân loại sản phẩm nội thất.  
> **Đơn vị thực tập:** Công ty TNHH Công nghệ và Dịch vụ Tin học An Bình.

---

## 📌 1. Giới Thệu Tổng Quan

Dự án xây dựng một hệ thống học sâu (Deep Learning) kết hợp ứng dụng Web hoàn chỉnh phục vụ phân loại tự động **6 danh mục sản phẩm nội thất phổ biến**:
- 🪑 **Ghế quầy bar** (`bar_stool`)
- 🛏️ **Giường ngủ** (`bed`)
- 🛋️ **Ghế tựa** (`chair`)
- ☕ **Bàn trà** (`coffee_table`)
- 🍽️ **Bàn ăn** (`dining_table`)
- 🗄️ **Tủ trang điểm** (`dresser`)

### ✨ Tính Năng Nổi Bật:
1. **Phân loại ảnh đa mô hình:** Hỗ trợ suy luận 3 kiến trúc CNN tiền huấn luyện (*MobileNetV2, ResNet18, EfficientNet-B0*) với độ chính xác tập kiểm thử vượt **>94%**.
2. **Trực quan hóa vùng chú ý Grad-CAM (XAI):** Hiển thị bản đồ nhiệt (Heatmap Colormap Jet) thể hiện các đường nét đặc trưng (*chân ghế, mặt bàn, thành giường*) mà mạng nơ-ron tập trung khi đưa ra dự đoán.
3. **Phát hiện dữ liệu ngoài phân bố (OOD Exception Detection):** Áp dụng kỹ thuật *Temperature Scaling ($T=2.5$)*, *Logit Margin* và *Softmax Entropy Filter* giúp tự động phát hiện và loại bỏ các hình ảnh không phải đồ nội thất (*ảnh người, xe cộ, động vật*).
4. **Giao diện Web hiện đại:** Thiết kế chuẩn Single Page Application (SPA) bằng Vue 3, Tailwind CSS tông màu sáng Pastel tươi tắn, hỗ trợ kéo thả ảnh, bộ mẫu 1-Click và biểu đồ so sánh chỉ số tương tác (Chart.js).

---

## 📁 2. Cấu Trúc Thư Mục Dự Án

```text
├── dataset/                     # Thư mục bộ dữ liệu (10,364 ảnh chia 70/15/15)
│   ├── train/                   # Tập huấn luyện (7,252 ảnh)
│   ├── val/                     # Tập kiểm định (1,553 ảnh)
│   └── test/                    # Tập kiểm thử (1,559 ảnh)
├── weights/                     # Thư mục lưu tệp trọng số Fine-tuned (.pth)
│   ├── mobilenet_v2.pth
│   ├── resnet18.pth
│   └── efficientnet_b0.pth
├── logs/                        # Thư mục nhật ký và tệp CSV chỉ số thực nghiệm
│   └── model_comparison.csv
├── plots/                       # Các biểu đồ đồ thị thực nghiệm (.png)
├── main.py                      # FastAPI Backend RESTful API Server & Grad-CAM Engine
├── train.py                     # Script huấn luyện Fine-tuning 2 giai đoạn (30 Epochs)
├── plot_metrics.py              # Script tự động vẽ 4 loại biểu đồ đồ thị báo cáo
├── process_data.py              # Script tiền xử lý và chia tập dữ liệu
└── frontend/                    # Ứng dụng Web Frontend (Vue 3 + Vite + Tailwind CSS)
    ├── src/
    │   ├── views/               # Các trang giao diện (Home, Prediction, Comparison, About)
    │   └── services/api.ts      # Dịch vụ kết nối RESTful API với Backend
    ├── package.json
    └── vite.config.ts
```

---

## 🛠️ 3. Yêu Cầu Môi Trường (Prerequisites)

- **Hệ điều hành:** Windows 10/11, Linux, hoặc macOS.
- **Python:** Phiên bản `3.11` (Khuyên dùng quản lý bằng Miniconda hoặc Anaconda).
- **Node.js:** Phiên bản `18.x` trở lên và `npm`.
- **Card đồ họa (GPU):** NVIDIA GPU hỗ trợ CUDA (Tùy chọn, hệ thống tự động chuyển sang CPU nếu không có GPU).

---

## 🚀 4. Hướng Dẫn Cài Đặt & Khởi Chạy Hệ Thống

### 🔹 Bước 1: Khởi Tạo Môi Trường Python (Backend)

Mở **Terminal / Anaconda Prompt** và chạy các lệnh sau:

```bash
# 1. Tạo môi trường ảo Conda với Python 3.11
conda create -n furniture_env python=3.11 -y

# 2. Kích hoạt môi trường
conda activate furniture_env

# 3. Cài đặt các thư viện Python cốt lõi
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install fastapi uvicorn python-multipart opencv-python pillow pandas numpy scikit-learn matplotlib seaborn
```

### 🔹 Bước 2: Khởi Chạy Máy Chủ Backend FastAPI

Tại thư mục gốc của dự án, chạy lệnh:

```bash
# Kích hoạt môi trường (nếu chưa kích hoạt)
conda activate furniture_env

# Chạy máy chủ Backend API
python main.py
```
> 🌐 Máy chủ Backend sẽ khởi chạy tại: `http://localhost:8000`  
> 📖 Tài liệu API Swagger UI tự động: `http://localhost:8000/docs`

---

### 🔹 Bước 3: Cài Đặt & Khởi Chạy Giao Diện Web Frontend

Mở một **Terminal mới**, di chuyển vào thư mục `frontend` và cài đặt gói thư viện:

```bash
# 1. Di chuyển vào thư mục giao diện web
cd frontend

# 2. Cài đặt các phụ thuộc npm
npm install

# 3. Khởi chạy máy chủ phát triển Frontend
npm run dev
```
> 🌐 Giao diện Web sẽ khởi chạy tại: `http://localhost:5173`

Bây giờ bạn có thể truy cập `http://localhost:5173` trên trình duyệt web để bắt đầu trải nghiệm ứng dụng phân loại sản phẩm nội thất và xem bản đồ nhiệt Grad-CAM!

---

## 📊 5. Các Lệnh Huấn Luyện & Vẽ Biểu Đồ (Dành cho nhà phát triển)

Nếu bạn muốn huấn luyện lại mô hình hoặc tự động vẽ lại các biểu đồ đồ thị cho báo cáo:

```bash
# Kích hoạt môi trường
conda activate furniture_env

# 1. Huấn luyện lại 3 mô hình (30 Epochs, Fine-tuning 2 giai đoạn)
python train.py

# 2. Tự động vẽ và xuất 4 loại biểu đồ đồ thị lưu vào thư mục plots/
python plot_metrics.py
```

---

## 🏆 6. Kết Quả Thực Nghiệm Đạt Được

| Kiến trúc Mô hình | Accuracy (Độ chính xác) | Precision | Recall | F1-Score | ROC-AUC | Inference Time (GPU) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **MobileNetV2** *(Khuyên dùng)* | **94.55%** | **94.45%** | **94.55%** | **94.43%** | **99.61%** | **22.4 ms** |
| **ResNet18** | 94.48% | 94.28% | 94.48% | 94.29% | 99.58% | 38.5 ms |
| **EfficientNet-B0** | 94.16% | 93.97% | 94.16% | 94.03% | 99.63% | 46.2 ms |

---

## 📝 7. Tác Giả & Lời Cảm Ơn

- **Sinh viên thực hiện:** Đồ án Thực tập Tốt nghiệp ngành CNTT.
- **Đơn vị thực tập:** Công ty TNHH Công nghệ và Dịch vụ Tin học An Bình.
- **Giáo viên hướng dẫn:** ThS. Nguyễn Thị Huệ / ThS. Phạm Thị Thanh Mai.
