TRƯỜNG ĐẠI HỌC KIẾN TRÚC HÀ NỘI

**KHOA CÔNG NGHỆ THÔNG TIN**

─────── \*\*\* ───────

**BÁO CÁO THỰC TẬP TỐT NGHIỆP**

![](data:image/png;base64...)

**ĐỀ TÀI: NGHIÊN CỨU, ỨNG DỤNG MẠNG NƠ-RON TÍCH CHẬP (CNN) TRONG BÀI TOÁN PHÂN LOẠI
SẢN PHẨM NỘI THẤT**

**Giảng** **viên** **hướng** **dẫn**: Th.S Phạm Thị Thanh Mai

**Sinh** **viên** **thực** **hiện**: Trương Thành Nam

**Lớp**: 22CN5

**Hà Nội, 9/2026**

# MỤC LỤC

[MỤC LỤC 1](#_Toc236586970)

[LỜI MỞ ĐẦU 4](#_Toc236586971)

[DANH MỤC HÌNH ẢNH 5](#_Toc236586972)

[DANH MỤC BẢNG BIỂU 6](#_Toc236586973)

[DANH MỤC TỪ VIẾT TẮT 7](#_Toc236586974)

[PHẦN 1: TỔNG QUAN VỀ ĐƠN VỊ THỰC TẬP VÀ ĐỀ TÀI 8](#_Toc236586975)

[1.1. Giới thiệu về doanh nghiệp thực tập 8](#_Toc236586976)

[1.2. Tóm tắt quá trình thực tập 8](#_Toc236586977)

[1.3. Tổng quan về đề tài thực tập 8](#_Toc236586978)

[1.3.1. Tính cấp thiết và bối cảnh thực tiễn của đề tài 8](#_Toc236586979)

[1.3.2. Mục tiêu nghiên cứu và đối tượng của đề tài 8](#_Toc236586980)

[1.3.3. Phạm vi nghiên cứu và phương pháp tiếp cận 8](#_Toc236586981)

[PHẦN 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ SỬ DỤNG 9](#_Toc236586982)

[2.1. Tổng quan về trí tuệ nhân tạo và thị giác máy tính 9](#_Toc236586983)

[2.1.1. Khái niệm AI, Machine Learning và Deep Learning 9](#_Toc236586984)

[2.1.2. Mạng nơ-ron tích chập (CNN) 9](#_Toc236586985)

[2.2. Ứng dụng mô hình CNN trong nhận diện biển báo giao thông 9](#_Toc236586986)

[2.2.1. Các lớp thành phần chính 9](#_Toc236586987)

[2.2.2. Kỹ thuật học chuyển giao (Transfer Learning) và Fine-tuning 9](#_Toc236586988)

[2.3. Các kiến trúc mạng cnn tiền huấn luyện được nghiên cứu 9](#_Toc236586989)

[2.3.1. Kiến trúc MobileNetV2 9](#_Toc236586990)

[2.3.2. Kiến trúc ResNet18 9](#_Toc236586991)

[2.3.3. Kiến trúc EfficientNet-B0 9](#_Toc236586992)

[2.4. Phương pháp giải thích trực quan mô hình với grad-cam 9](#_Toc236586993)

[2.4.1. Khái niệm và vai trò của Explainable AI (XAI) trong Deep Learning 9](#_Toc236586994)

[2.4.2. Nguyên lý hoạt động của kỹ thuật Grad-CAM 9](#_Toc236586995)

[2.5. Các công nghệ và thư viện phát triển hệ thống 9](#_Toc236586996)

[2.5.1. Ngôn ngữ Python và thư viện Machine Learning 9](#_Toc236586997)

[2.5.2. Môi trường Backend API 9](#_Toc236586998)

[2.5.3. Môi trường Frontend UI 9](#_Toc236586999)

[PHẦN 3: NỘI DUNG THỰC TẬP 10](#_Toc236587000)

[3.1. Quy trình chuẩn bị và tiền xử lý dữ liệu 10](#_Toc236587001)

[3.1.1. Thu thập và cấu trúc bộ dữ liệu ảnh nội thất 10](#_Toc236587002)

[3.1.2. Phân chia tập dữ liệu 10](#_Toc236587003)

[3.1.3. Chuẩn hóa hình ảnh và Tăng cường dữ liệu 10](#_Toc236587004)

[3.2. Quy trình huấn lượng mô hình 2 giai đoạn 10](#_Toc236587005)

[3.2.1. Giai đoạn 1 10](#_Toc236587006)

[3.2.2. Giai đoạn 2 10](#_Toc236587007)

[3.2.3. Thiết lập hàm mất mát và bộ tối ưu hóa 10](#_Toc236587008)

[3.3. Cài đặt thuật toán trực quan hóa grad-cam 10](#_Toc236587009)

[3.3.1. Xác định Lớp mục tiêu cho từng mô hình 10](#_Toc236587010)

[3.3.2. Thiết lập PyTorch Hooks trích xuất Feature Maps và Gradients 10](#_Toc236587011)

[3.3.3. Tạo bản đồ nhiệt Colormap Jet, phủ ảnh gốc và mã hóa Base64 Data URL 10](#_Toc236587012)

[3.4. Cơ chế xử lý ngoại lệ phát hiện dữ liệu ngoài phân bố 10](#_Toc236587013)

[3.4.1. Phân tích hạn chế của hàm Softmax đối với ảnh không thuộc các danh mục 10](#_Toc236587014)

[3.4.2. Xây dựng thuật toán kiểm tra ngưỡng tin cậy 10](#_Toc236587015)

[3.5. Xây dựng hệ thống ứng dụng web 10](#_Toc236587016)

[3.5.1. Phân tích yêu cầu và sơ đồ kiến trúc hệ thống Client - Server RESTful API 10](#_Toc236587017)

[3.5.2. Phát triển RESTful API backend với FastAPI 10](#_Toc236587018)

[3.5.3. Phát triển giao diện người dùng frontend với Vue 3 + Tailwind CSS 10](#_Toc236587019)

[CHƯƠNG 4. THỰC NGHIỆM, ĐÁNH GIÁ KẾT QUẢ VÀ BÀN LUẬN 11](#_Toc236587020)

[4.1. Môi trường thực nghiệm và thông số phần cứng 11](#_Toc236587021)

[4.1.1. Cấu hình phần cứng 11](#_Toc236587022)

[4.1.2. Môi trường phần mềm 11](#_Toc236587023)

[4.2. Đánh giá các mô hình trên 6 chỉ số thực nghiệm 11](#_Toc236587024)

[4.3. Phân tích kết quả thực nghiệm qua biểu đồ trực quan 11](#_Toc236587025)

[Biểu đồ đường học (Learning Curves: Train/Val Loss & Accuracy qua 30 Epochs) 11](#_Toc236587026)

[Ma trận nhầm lẫn (Confusion Matrix Heatmaps) 11](#_Toc236587027)

[Đường cong ROC và Precision-Recall Curves 11](#_Toc236587028)

[Đánh giá tốc độ suy luận (Inference Time ms) và dung lượng mô hình 11](#_Toc236587029)

[4.4. Đánh giá khả năng giải thích grad-cam và xử lý ngoại lệ ood 11](#_Toc236587030)

[4.4.1. Phân tích bản đồ nhiệt Grad-CAM trên các sản phẩm nội thất thực tế 11](#_Toc236587031)

[4.4.2. Đánh giá hiệu quả lọc ảnh người và ảnh ngoại lệ với ngưỡng 80% 11](#_Toc236587032)

[CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN 12](#_Toc236587033)

[5.1. Kết quả đạt được của đề tài 12](#_Toc236587034)

[5.1.1. Về mặt lý thuyết và nghiên cứu 12](#_Toc236587035)

[5.1.2. Về mặt sản phẩm thực tế 12](#_Toc236587036)

[5.1.3. Về mặt số liệu thực nghiệm 12](#_Toc236587037)

[5.2. Hạn chế và khó khăn còn tồn tại 12](#_Toc236587038)

[5.2.1. Hạn chế về số lượng lớp nội thất 12](#_Toc236587039)

[5.2.2. Thách thức với các góc chụp ảnh bị che khuất hoặc ánh sáng quá yếu 12](#_Toc236587040)

[5.3. Hướng phát triển trong tương lai 12](#_Toc236587041)

[5.3.1. Mở rộng tập dữ liệu thêm nhiều danh mục đồ nội thất khác 12](#_Toc236587042)

[5.3.2. Triển khai mô hình phát hiện đối tượng đa mục tiêu (Object Detection với YOLOv8) trên ảnh toàn cảnh phòng khách/phòng ngủ 12](#_Toc236587043)

[5.3.3. Đóng gói Container với Docker và triển khai lên môi trường Cloud (AWS / GCP / Vercel) 12](#_Toc236587044)

[KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN 13](#_Toc236587045)

[TÀI LIỆU THAM KHẢO 15](#_Toc236587046)

# LỜI MỞ ĐẦU

Trong bối cảnh giao thông đô thị ngày càng phức tạp, việc nâng cao hiệu quả quản lý và đảm bảo an toàn giao thông trở thành một trong những nhiệm vụ cấp thiết. Nhận thấy tiềm năng của trí tuệ nhân tạo trong lĩnh vực giao thông, doanh nghiệp đã tập trung nghiên cứu và ứng dụng các giải pháp công nghệ mới nhằm hỗ trợ việc phát hiện và phân loại biển báo giao thông. Trong đó, mô hình mạng nơ-ron tích chập (CNN - Convolutional Neural Network) được lựa chọn như một công cụ mạnh mẽ để nhận diện hình ảnh biển báo một cách tự động và chính xác.

Đề tài này tập trung tìm hiểu cách doanh nghiệp VINAI triển khai ứng dụng CNN vào hệ thống nhận diện biển báo giao thông, đồng thời tích hợp với chức năng cảnh báo mức xử phạt theo các quy định pháp luật Việt Nam. Trên cơ sở phân tích các loại biển báo (biển cấm, biển báo nguy hiểm, biển chỉ dẫn, biển hiệu lệnh), đề tài mong muốn xây dựng một kết nối giữa công nghệ nhận diện và phần mềm quản lý xử phạt – từ việc nhận biết biển báo đến việc thông báo chủ phương tiện về hậu quả hành chính nếu vi phạm. Qua đó, nghiên cứu sẽ làm rõ khả năng ứng dụng thực tế của công nghệ AI trong lĩnh vực giao thông, cũng như đánh giá hiệu quả và những thách thức khi triển khai tại thị trường Việt Nam.

Hy vọng rằng với kết quả của nghiên cứu của nhóm không chỉ đóng góp về mặt học thuật mà còn mang lại giá trị thực tiễn cho công tác quản lý giao thông thông minh, hướng tới mô hình “đô thị thông minh” và “giao thông hiệu quả” – nơi mỗi biển báo không chỉ là tín hiệu hình ảnh mà còn là phần của hệ thống cảnh báo, giám sát và xử lý vi phạm.

# DANH MỤC HÌNH ẢNH

# DANH MỤC BẢNG BIỂU

# DANH MỤC TỪ VIẾT TẮT

|  |  |  |
| --- | --- | --- |
| **STT** | **Từ** **viết** **tắt** | **Tên** **đầy** **đủ** |
| 1 | AI | Artificial Intelligence |
| 2 | ASI | Artificial Superintelligence |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

# PHẦN 1: TỔNG QUAN VỀ ĐƠN VỊ THỰC TẬP VÀ ĐỀ TÀI

## 1.1. Giới thiệu về doanh nghiệp thực tập

## 1.2. Tóm tắt quá trình thực tập

## 1.3. Tổng quan về đề tài thực tập

### 1.3.1. Tính cấp thiết và bối cảnh thực tiễn của đề tài

### 1.3.2. Mục tiêu và phạm vi nghiên cứu của đề tài

# PHẦN 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ SỬ DỤNG

## 2.1. Tổng quan về trí tuệ nhân tạo và học sâu (Deep Learning)

### 2.1.1. Khái niệm về trí tuệ nhân tạo và học sâu (Deep Learning)

**CNN (Convolutional Neural Network)** là một loại mạng nơ-ron nhân tạo được ứng dụng phổ biến trong lĩnh vực **Học sâu (Deep Learning)**, đặc biệt là trong **Thị giác máy tính (Computer Vision)**. Mạng CNN có khả năng tự động trích xuất và học các đặc trưng của hình ảnh, nhờ đó được sử dụng rộng rãi trong các bài toán như nhận diện và phân loại ảnh, nhận diện khuôn mặt, phát hiện đối tượng, cùng nhiều ứng dụng khác trong công nghệ và các lĩnh vực liên quan.

### 2.1.2. Khái niệm và ứng dụng của Thị giác máy tính

## 2.2. Ứng dụng mô hình CNN trong nhận diện biển báo giao thông

### 2.2.1. Các lớp thành phần chính

### 2.2.2. Kỹ thuật học chuyển giao (Transfer Learning) và Fine-tuning

## 2.3. Các kiến trúc CNN tiền huấn luyện được nghiên cứu

### 2.3.1. Kiến trúc MobileNetV2

### 2.3.2. Kiến trúc ResNet18

### 2.3.3. Kiến trúc EfficientNet-B0

## 2.4. Kỹ thuật trực quan hóa Grad-CAM

# PHẦN 3: NỘI DUNG THỰC TẬP

## 3.1. Quy trình chuẩn bị và tiền xử lý dữ liệu

### 3.1.1. Thu thập và cấu trúc bộ dữ liệu ảnh nội thất

### 3.1.2. Phân chia tập dữ liệu và tăng cường dữ liệu

## 3.2. Quy trình huấn lượng mô hình

### 3.2.1. Chiến lược Fine-tuning 2 giai đoạn

### 3.2.2. Thiết lập thông số huấn luyện

## 3.3. Cơ chế xử lý ngoại lệ phát hiện ảnh ngoài phân bố

### 3.3.1. Nguyên lý lọc ảnh ngoài danh mục

### 3.3.2. Thiết lập ngưỡng tin cậy

## 3.4. Xây dựng ứng dụng Web thử nghiệm mô hình

# CHƯƠNG 4. THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ

## 4.1. Môi trường thực nghiệm và thông số phần cứng

## 4.2. Đánh giá kết quả huấn luyện và so sánh 3 mô hình

So sánh trên 6 chỉ số (Accuracy, Precision, Recall, F1-Score, ROC-AUC, PR-AUC)

Phân tích qua biểu đồ (Learning Curves, Confusion Matrix, ROC/PR Curves)

Đánh giá thực tế tính năng Grad-CAM và Cảnh báo ngoại lệ OOD

# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

**Kết quả đạt được:**

**Những điều còn hạn chế:**

**Hướng phát triển trong tương lai:**

**Kết luận:**

# TÀI LIỆU THAM KHẢO

1. GS. TS Từ Minh Phương, *Giáo trình Nhập môn Trí tuệ nhân tạo, Học viện CN BCVT, 2020*
2. https://viblo.asia/p/deep-learning-tim-hieu-ve-mang-tich-chap-cnn-maGK73bOKj2
3. https://www.youtube.com/watch?v=rmNTqYGpr6Y&t=362s
4. https://vi.wikipedia.org/wiki/Bi%E1%BB%83n\_b%C3%A1o\_giao\_th%C3%B4ng\_t%E1%BA%A1i\_Vi%E1%BB%87t\_Nam
5. https://cdn.thuvienphapluat.vn/phap-luat/2022-2/CTNN/quy-chuan-ky-thuat-qcvn-41-2019-bgtvt-bao-hieu-duong-bo.pdf
6. https://thuvienphapluat.vn/iThong/tra-cuu-xu-phat-giao-thong.aspx