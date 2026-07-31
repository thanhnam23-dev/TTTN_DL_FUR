# Kế hoạch thực hiện đồ án thực tập

## Đề tài

**Xây dựng hệ thống phân loại sản phẩm nội thất sử dụng Deep Learning**

## 1. Mục tiêu

-   Upload ảnh nội thất.
-   Nhận diện loại sản phẩm.
-   Hiển thị Top-3 dự đoán.
-   Hiển thị Confidence.
-   Hiển thị Inference Time.
-   Hiển thị Grad-CAM.

## 2. Dataset

-   Furniture Dataset for Multi-Angle AI Training
-   https://www.kaggle.com/datasets/oortdatahub/furniture-dataset-for-multi-angle-ai-training

## 3. Tiền xử lý

-   Resize 224x224
-   Normalize ImageNet
-   Train/Validation/Test = 70/15/15
-   Augmentation: Flip, Rotate, Crop, Color Jitter

## 4. Mô hình

### MobileNetV2

-   Baseline
-   Nhanh, nhẹ

### ResNet18

-   CNN kinh điển

### EfficientNet-B0

-   Accuracy tốt

## 5. Fine-tuning

### Giai đoạn 1

-   Freeze backbone
-   Train FC
-   Epoch: 5--10
-   LR: 1e-3

### Giai đoạn 2

-   Unfreeze các block cuối
-   Epoch: 15--20
-   LR: 1e-5

## 6. Đánh giá

-   Accuracy
-   Precision
-   Recall
-   F1-score
-   Confusion Matrix

So sánh 3 mô hình và chọn mô hình tốt nhất.

## 7. Kiến trúc

Frontend: - Vue 3 - TypeScript - Tailwind CSS - PrimeVue

Backend: - FastAPI - PyTorch

Deploy: - Frontend: Vercel - Backend: Railway hoặc Render

## 8. Chức năng Website

### Home

-   Giới thiệu đề tài

### Prediction

-   Upload ảnh
-   Xem ảnh đã tải
-   Top-3 dự đoán
-   Confidence
-   Inference Time
-   Grad-CAM
-   Model đang sử dụng

### Model Comparison

-   So sánh Accuracy, Precision, Recall, F1-score của MobileNetV2,
    ResNet18 và EfficientNet-B0.

### About

-   Dataset
-   Quy trình huấn luyện
-   Công nghệ sử dụng

## 9. Tiến độ

### Tuần 1

-   Chuẩn bị dataset
-   Tiền xử lý
-   Augmentation

### Tuần 2

-   Huấn luyện 3 mô hình
-   Fine-tune

### Tuần 3

-   Đánh giá
-   Xây dựng API
-   Xây dựng giao diện

### Tuần 4

-   Tích hợp
-   Deploy
-   Kiểm thử
-   Hoàn thiện báo cáo

## 10. Kết quả kỳ vọng

-   Accuracy \>95%
-   So sánh 3 mô hình
-   Website hoàn chỉnh
-   Demo online
