TRƯỜNG ĐẠI HỌC KIẾN TRÚC HÀ NỘI

**KHOA CÔNG NGHỆ THÔNG TIN**

─────── \*\*\* ───────

**ĐỒ** **ÁN MÔN** **THỰC TẬP CHUYÊN MÔN I**

![](data:image/png;base64...)

NHÓM 5

**ĐỀ TÀI: TÌM HIỂU DOANH NGHIỆP VINAI VÀ ỨNG DỤNG MÔ HÌNH CNN TRONG NHẬN DIỆN BIỂN BÁO GIAO THÔNG VÀ CẢNH BẢO MỨC XỬ PHẠT THEO QUY ĐỊNH PHÁP LUẬT VIỆT NAM**

**Giảng** **viên** **hướng** **dẫn** : Th.S Nguyễn Thị Huệ

**Nhóm** **sinh** **viên** **thực** **hiện** : Bùi Quang Khải

Nguyễn Hoàng Anh

Bùi Kim Đạt

Âu Xuân Mạnh

Trương Thành Nam

**Hà Nội, 10/2025**

# MỤC LỤC

[**MỤC LỤC 1**](#_Toc212564091)

[**LỜI MỞ ĐẦU 3**](#_Toc212564092)

[**DANH MỤC HÌNH ẢNH 4**](#_Toc212564093)

[**DANH MỤC BẢNG BIỂU 5**](#_Toc212564094)

[**DANH MỤC TỪ VIẾT TẮT 6**](#_Toc212564095)

[**PHẦN 1: GIỚI THIỆU VỀ ĐƠN VỊ THỰC TẬP VÀ CƠ SỞ LÝ THUYẾT 7**](#_Toc212564096)

[1.1. Giới thiệu về công ty 7](#_Toc212564097)

[1.1.2. Tổng quan về dự án của công ty 8](#_Toc212564098)

[1.1.3. Giới thiệu về dự án thực tập 8](#_Toc212564099)

[1.2. Tổng quan về trí tuệ nhân tạo 9](#_Toc212564100)

[1.2.1. Khái niệm về trí tuệ nhân tạo 9](#_Toc212564101)

[1.2.2. Các hướng nghiên cứu về trí tuệ nhân tạo 9](#_Toc212564102)

[1.2.3. Phân loại trí tuệ nhân tạo 10](#_Toc212564103)

[1.3. Tổng quan về Thị giác máy tính 10](#_Toc212564104)

[1.3.1. Khái niệm về thị giác máy tính 10](#_Toc212564105)

[1.3.2. Các bài toán cơ bản trong Thị giác máy tính 10](#_Toc212564106)

[1.3.3. Ứng dụng của Thị giác máy tính 11](#_Toc212564107)

[1.4. Giới thiệu về đề tài 11](#_Toc212564108)

[1.4.1. Mô tả đề tài 11](#_Toc212564109)

[1.4.2. Giới thiệu về chức năng 11](#_Toc212564110)

[**PHẦN 2: GIỚI THIỆU MÔ HÌNH CNN VÀ QUY TRÌNH TRIỂN KHAI NHẬN DIỆN BIỂN BÁO GIAO THÔNG 13**](#_Toc212564111)

[2.1. Giới thiệu về mô hình CNN 13](#_Toc212564112)

[2.1.1. Khái niệm mô hình 13](#_Toc212564113)

[2.1.2. Các lớp chính trong mô hình 13](#_Toc212564114)

[2.2. Ứng dụng mô hình CNN trong nhận diện biển báo giao thông 13](#_Toc212564115)

[2.2.1. Chuẩn bị dữ liệu và tiền xử lý dữ liệu 13](#_Toc212564116)

[2.2.1.1. Chuẩn bị dữ liệu 13](#_Toc212564117)

[2.2.1.2. Tiền xử lý dữ liệu 15](#_Toc212564118)

[2.2.2. Trích xuất đặc trưng 17](#_Toc212564119)

[2.2.3. Huấn luyện mô hình 18](#_Toc212564120)

[**PHẦN 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ 20**](#_Toc212564121)

[3.1. Giới thiệu về các công nghệ sử dụng trong đề tài 20](#_Toc212564122)

[3.1.1. Các công cụ hỗ trợ 20](#_Toc212564123)

[3.1.2. Các thư viện hỗ trợ 20](#_Toc212564124)

[3.2. Phân tích hệ thống xử lý 21](#_Toc212564125)

[3.3. Triển khai/ Sử dụng hệ thống 21](#_Toc212564126)

[3.3.1. Chuẩn bị các tệp dữ liệu 21](#_Toc212564127)

[3.3.2. Khởi chạy ứng dụng 22](#_Toc212564128)

[3.3.3. Dự đoán biển báo với mô hình đã lưu 22](#_Toc212564129)

[3.4. Đánh giá kết quả thực nghiệm 23](#_Toc212564130)

[**KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN 26**](#_Toc212564131)

[**TÀI LIỆU THAM KHẢO 28**](#_Toc212564132)

[**BẢNG PHÂN CHIA CÔNG VIỆC 29**](#_Toc212564133)

# LỜI MỞ ĐẦU

Trong bối cảnh giao thông đô thị ngày càng phức tạp, việc nâng cao hiệu quả quản lý và đảm bảo an toàn giao thông trở thành một trong những nhiệm vụ cấp thiết. Nhận thấy tiềm năng của trí tuệ nhân tạo trong lĩnh vực giao thông, doanh nghiệp đã tập trung nghiên cứu và ứng dụng các giải pháp công nghệ mới nhằm hỗ trợ việc phát hiện và phân loại biển báo giao thông. Trong đó, mô hình mạng nơ-ron tích chập (CNN - Convolutional Neural Network) được lựa chọn như một công cụ mạnh mẽ để nhận diện hình ảnh biển báo một cách tự động và chính xác.

Đề tài này tập trung tìm hiểu cách doanh nghiệp VINAI triển khai ứng dụng CNN vào hệ thống nhận diện biển báo giao thông, đồng thời tích hợp với chức năng cảnh báo mức xử phạt theo các quy định pháp luật Việt Nam. Trên cơ sở phân tích các loại biển báo (biển cấm, biển báo nguy hiểm, biển chỉ dẫn, biển hiệu lệnh), đề tài mong muốn xây dựng một kết nối giữa công nghệ nhận diện và phần mềm quản lý xử phạt – từ việc nhận biết biển báo đến việc thông báo chủ phương tiện về hậu quả hành chính nếu vi phạm. Qua đó, nghiên cứu sẽ làm rõ khả năng ứng dụng thực tế của công nghệ AI trong lĩnh vực giao thông, cũng như đánh giá hiệu quả và những thách thức khi triển khai tại thị trường Việt Nam.

Hy vọng rằng với kết quả của nghiên cứu của nhóm không chỉ đóng góp về mặt học thuật mà còn mang lại giá trị thực tiễn cho công tác quản lý giao thông thông minh, hướng tới mô hình “đô thị thông minh” và “giao thông hiệu quả” – nơi mỗi biển báo không chỉ là tín hiệu hình ảnh mà còn là phần của hệ thống cảnh báo, giám sát và xử lý vi phạm.

# DANH MỤC HÌNH ẢNH

[Hình 1.1. Công ty nghiên cứu và phát triển AI - VinAI 7](#_Toc216476044)

[Hình 2.1. Ảnh chụp thực tế 14](#_Toc216476045)

[Hình 2.2. Hình chụp từ GoogleMaps 14](#_Toc216476046)

[Hình 2.3. Dựng biển báo trong Blender 15](#_Toc216476047)

[Hình 2.4. Biển báo sau khi được thu thập 15](#_Toc216476048)

[Hình 2.5. Quá trình xử lý dữ liệu 16](#_Toc216476049)

[Hình 2.6. Phân loại và Resize ảnh 17](#_Toc216476050)

[Hình 2.7. Thông tin đặc trưng của biển báo 18](#_Toc216476051)

[Hình 2.8. Huấn luyện mô hình 19](#_Toc216476052)

[Hình 3.1. Biểu đô UseCase tổng quát 21](#_Toc216476053)

[Hình 3.2. Các tệp dữ liệu cần thiết 22](#_Toc216476054)

[Hình 3.3. Nhận diện biển báo 23](#_Toc216476055)

[Hình 3.4. Kết quả khi nhận diện biển báo 23](#_Toc216476056)

[Hình 3.5. Biểu đồ độ chính xác huấn luyện và kiểm định của mô hình 24](#_Toc216476057)

[Hình 3.6. Biểu đồ hàm mất mát trên tập huấn luyện và kiểm định của mô hình 25](#_Toc216476058)

# DANH MỤC BẢNG BIỂU

[Bảng 3.1. Kết quả dự đoán trên một số biển báo 24](#_Toc216476097)

[Bảng 3.2. So sánh giá trị các epochs 25](#_Toc216476098)

# DANH MỤC TỪ VIẾT TẮT

|  |  |  |
| --- | --- | --- |
| **STT** | **Từ** **viết** **tắt** | **Tên** **đầy** **đủ** |
| 1 | AI | Artificial Intelligence |
| 2 | ASI | Artificial Superintelligence |
| 3 | CORS | Cross-Origin Resource Sharing |
| 4 | CNN | Convolutional Neural Network |
| 5 | CSS | Cascading Style Sheets |
| 6 | CSV | Comma-Separated Values |
| 7 | DMS | Document Management System |
| 8 | HTML | HyperText Markup Language |
| 9 | MIT | Massachusetts Institute of Technology |
| 10 | SSD | Single Shot MultiBox Detector |
| 11 | YOLO | You Only Look Once |
| 12 | IBM | International Business Machines |

# PHẦN 1: GIỚI THIỆU VỀ ĐƠN VỊ THỰC TẬP VÀ CƠ SỞ LÝ THUYẾT

## 1.1. Giới thiệu về công ty

VinAI Research (VinAI) là công ty nghiên cứu và phát triển trí tuệ nhân tạo hàng đầu tại Việt Nam, trực thuộc Tập đoàn Vingroup. Thành lập vào năm 2019, VinAI định hướng trở thành trung tâm nghiên cứu AI mang tầm khu vực và thế giới, tập trung vào việc phát triển công nghệ lõi và ứng dụng AI vào các sản phẩm thực tiễn.

![Vingroup thành lập Viện trí tuệ nhân tạo (VinAI), nghiên cứu những vấn đề  tầm cỡ thế giới](data:image/jpeg;base64...)

Hình 1.1. Công ty nghiên cứu và phát triển AI - VinAI

VinAI hiện có trụ sở chính tại Hà Nội và các văn phòng nghiên cứu ở TP. Hồ Chí Minh, Mỹ và Úc. Đội ngũ của VinAI gồm hơn 200 chuyên gia, kỹ sư, và nhà nghiên cứu đến từ nhiều quốc gia, trong đó có các tiến sĩ tốt nghiệp tại những trường đại học hàng đầu thế giới như Stanford, MIT, Oxford, và các chuyên gia từng làm việc tại Google, Microsoft, hay NVIDIA.

Các hướng nghiên cứu chính của VinAI bao gồm:

Machine Learning (Học máy)

Computer Vision (Thị giác máy tính)

Natural Language Processing (Xử lý ngôn ngữ tự nhiên)

Speech Processing (Xử lý giọng nói)

AI cho xe tự hành và robot thông minh

Bên cạnh hoạt động nghiên cứu, VinAI còn chú trọng đến việc chuyển giao công nghệ, triển khai các sản phẩm thương mại AI cho hệ sinh thái của Vingroup và các đối tác quốc tế.

### 1.1.2. Tổng quan về dự án của công ty

VinAI hiện đang phát triển nhiều dự án công nghệ AI ứng dụng trong thực tế, đặc biệt trong lĩnh vực ô tô thông minh, thành phố thông minh và sức khỏe số. Một số dự án tiêu biểu bao gồm:

**Driver Monitoring System (DMS):** Hệ thống giám sát người lái sử dụng camera và AI để phát hiện trạng thái mất tập trung, buồn ngủ hoặc sử dụng điện thoại khi lái xe. Sản phẩm này đã được ứng dụng trên các dòng xe VinFast, góp phần nâng cao an toàn giao thông.

**Face Recognition (Nhận diện khuôn mặt)**: Công nghệ nhận diện khuôn mặt của VinAI đạt chuẩn quốc tế, được ứng dụng trong bảo mật, chấm công, kiểm soát ra vào, và các giải pháp thông minh cho tòa nhà hoặc hệ thống thanh toán không chạm.

**AI Camera và Computer Vision:** Nghiên cứu và phát triển hệ thống camera thông minh hỗ trợ nhận dạng đối tượng, biển báo giao thông, phân tích hành vi – phục vụ cho xe tự hành và giám sát đô thị.

### 1.1.3. Giới thiệu về dự án thực tập

Dự án thực tập: Nhận diện cảm xúc khuôn mặt bằng trí tuệ nhân tạo (AI). Đây là một đề tài có tính thực tế cao, được ứng dụng trong nhiều lĩnh vực như chăm sóc khách hàng, giáo dục, an ninh hay phương tiện tự hành.

**Mục tiêu của dự án:**

Xây dựng mô hình có khả năng phân tích khuôn mặt người trong hình ảnh và video.

Xác định và phân loại cảm xúc của con người như vui, buồn, tức giận, ngạc nhiên, sợ hãi, bình thường...

**Kỹ năng học được trong quá trình thực tập:**

Hiểu rõ quy trình phát triển một mô hình AI từ dữ liệu đến triển khai.

Thành thạo hơn trong việc lập trình và sử dụng các công cụ như Google Colab, GitHub.

Rèn luyện kỹ năng làm việc nhóm, trình bày kết quả, và quản lý tiến độ dự án.

**Kết quả đạt được:**

Mô hình có thể nhận diện được các cảm xúc cơ bản với độ chính xác tương đối tốt.

Tích lũy được nhiều kinh nghiệm thực tế, củng cố kiến thức học thuật và định hướng nghề nghiệp rõ ràng hơn trong lĩnh vực AI.

## 1.2. Tổng quan về trí tuệ nhân tạo

### 1.2.1. Khái niệm về trí tuệ nhân tạo

Trí tuệ nhân tạo (AI) là một lĩnh vực nghiên cứu của khoa học máy tính và khoa học tính toán nói chung. Có nhiều quan điểm khác nhau về trí tuệ nhân tạo và do vậy có nhiều định nghĩa khác nhau về lĩnh vực khoa học này.

### 1.2.2. Các hướng nghiên cứu về trí tuệ nhân tạo

**Cảm nhận:**

Hệ thống trí tuệ nhân tạo (AI) cần có cơ chế thu nhận thông tin từ môi trường bên ngoài thông qua các thiết bị như camera, microphone, radar, và cảm biến gia tốc, hoặc thông tin do người dùng nhập vào. Để xử lý thông tin này, cần áp dụng các kỹ thuật trong các lĩnh vực sau:

**Thị giác máy (computer vision):**

Là lĩnh vực trí tuệ nhân tạo có mục đích nghiên cứu về thu nhận, xử lý và phân tích hình ảnh từ cảm biến như camera. Mục tiêu là chuyển đổi thông tin thành dạng mà máy tính có thể hiệu, ví dụ như từ ảnh văn bản thành mã UNICODE.

Các bài toán chính bao gồm: Nhận dạng mẫu (Pattern Recognition), Phân tích chuyển động (Motion Analysis), Tạo khung lập cảnh 3D (Scene Reconstruction).

**Nhận dạng mẫu:**

Là lĩnh vực nghiên cứu lớn nhất trong phạm vi thị giác máy bao gồm các bài toán như nhận dạng đối tượng, nhận dạng mặt người, vân tay và chữ viết.

Việc nhận dạng tự động thường khó hơn so với con người; máy tính hiện chỉ có khả năng nhận dạng một số lớp đối tượng với độ chính xác gần gũi con người.

**Xử lý ngôn ngữ tự nhiên (natural language processing):**

Đây là lĩnh vực nghiên cứu có mục đích phân tích thông tin dạng âm thanh hoặc văn bản bằng ngôn ngữ tự nhiên của con người. Cho phép người dùng giao tiếp với máy tính bằng cách nói, tương tự như giao tiếp với von người, điều này rất hữu ích

trong nhiều tình huống.

### 1.2.3. Phân loại trí tuệ nhân tạo

Trí tuệ nhân tạo (AI) có thể được phân loại theo nhiều tiêu chí khác nhau. Theo Arend Hintze, AI có thể chia thành các loại dựa trên sự tương đồng với trí tuệ con người:

**AI phản ứng (Reactive Machine):** Loại AI này chỉ có khả năng phân tích và đưa ra quyết định trong thời gian thực mà không có bộ nhớ. Ví dụ, chương trình cờ vua Deep Blue của IBM đã đánh bại Garry Kasparov vào những năm 1990.

**AI với bộ nhớ hạn chế:** AI này có thể sử dụng kinh nghiệm quá khứ để đưa ra quyết định trong tương lai. Một ứng dụng điển hình là AI trong xe tự lái, giúp dự đoán và điều chỉnh tốc độ để tránh va chạm.

**Lý thuyết về tâm trí:** AI có khả năng học hỏi và tự tư duy, nhưng chưa đạt được độ khả thi cao. Một ví dụ là AI do Facebook phát triển, tuy nhiên chúng đã tự tạo ra ngôn ngữ mới mà các chuyên gia không thể giải mã.

Ngoài ra, AI còn được phân thành ba loại dựa trên mức độ thông minh:

**Trí tuệ nhân tạo hẹp (Narrow AI):** Thực hiện nhiệm vụ cụ thể như nhận diện giọng nói hay chơi cờ. Không có khả năng tự học hay tự nhận thức.

**Trí tuệ nhân tạo mạnh (Strong AI):** Có khả năng tư duy và hoạt động như con người trong nhiều khía cạnh. Đây là mục tiêu nghiên cứu hiện nay.

**Trí tuệ nhân tạo siêu mạnh (Artificial Superintelligence – ASI):** Là AI vượt trội hơn cả trí tuệ con người, có khả năng thực hiện những công việc mà con người không thể làm. Đây vẫn là một khái niệm lý thuyết và chưa được phát triển thực tế.

## 1.3. Tổng quan về Thị giác máy tính

### 1.3.1. Khái niệm về thị giác máy tính

Thị giác máy (Computer Vision) là một lĩnh vực thuộc trí tuệ nhân tạo, nghiên cứu về việc thu nhận, xử lý, phân tích và nhận dạng thông tin hình ảnh thu được từ các cảm biến như camera. Mục tiêu của thị giác máy là chuyển đổi thông tin hình ảnh ở mức thấp thành biểu diễn ở mức cao hơn, giúp máy tính có thể “hiểu” nội dung của hình ảnh.

### 1.3.2. Các bài toán cơ bản trong Thị giác máy tính

Thị giác máy tính bao gồm nhiều bài toán quan trọng, trong đó có:

**Nhận dạng mẫu (Pattern Recognition):** Xác định và phân loại các đối tượng hoặc đặc trưng xuất hiện trong ảnh.

**Phân tích chuyển động (Motion Analysis):** Theo dõi và mô tả sự di chuyển của các vật thể trong chuỗi ảnh hoặc video.

**Tạo lập khung cảnh 3D (Scene Reconstruction):** Tái tạo cấu trúc không gian ba chiều của môi trường từ các ảnh hai chiều.

**Nâng cao chất lượng ảnh (Image Restoration):** Khôi phục hoặc cải thiện chất lượng ảnh bị nhiễu, mờ hoặc thiếu sáng.

### 1.3.3. Ứng dụng của Thị giác máy tính

Thị giác máy tính được ứng dụng rộng rãi trong nhiều lĩnh vực như giao thông thông minh, y học, nông nghiệp, an ninh và bán lẻ. Trong giao thông, công nghệ này hỗ trợ nhận diện biển báo, phát hiện vi phạm và trợ giúp lái xe an toàn (ADAS).

Trong đề tài này, thị giác máy tính được nhóm ứng dụng để nhận diện và cảnh báo biển báo giao thông, giúp hệ thống phân tích hình ảnh, xác định loại biển báo và cung cấp thông tin cảnh báo phù hợp, góp phần nâng cao an toàn giao thông.

## 1.4. Giới thiệu về đề tài

### 1.4.1. Mô tả đề tài

Trong bối cảnh giao thông ngày càng phức tạp và tai nạn do vi phạm biển báo vẫn diễn ra phổ biến, việc áp dụng công nghệ trí tuệ nhân tạo để nhận diện và cảnh báo biển báo giao thông là cần thiết. Đề tài **“Ứng dụng mô hình CNN trong nhận diện biển báo giao thông và cảnh báo mức xử phạt theo quy định pháp luật Việt Nam”** hướng đến việc xây dựng một hệ thống có khả năng nhận dạng tự động các loại biển báo giao thông từ hình ảnh.

Sau khi nhận diện thành công, hệ thống sẽ hiển thị thông tin chi tiết của biển báo, đồng thời cảnh báo mức xử phạt tương ứng nếu người điều khiển phương tiện vi phạm quy định liên quan đến biển báo đó. Mục tiêu của đề tài là hỗ trợ nâng cao ý thức người tham gia giao thông, góp phần giảm thiểu vi phạm và đảm bảo an toàn khi lưu thông trên đường.

### 1.4.2. Giới thiệu về chức năng

**Nhận diện biển báo giao thông:**

Ứng dụng được xây dựng nhằm hỗ trợ việc phân loại và nhận biết các biển báo giao thông tại Việt Nam thông qua công nghệ trí tuệ nhân tạo (AI), cụ thể là mô hình **CNN (Convolutional Neural Network)**. Hệ thống có khả năng phân tích hình ảnh biển báo được người dùng tải lên, từ đó tự động nhận diện và xác định chính xác loại biển báo, bao gồm:

**Biển cấm**: quy định các hành vi mà người tham gia giao thông không được phép thực hiện.

**Biển báo nguy hiểm (biển cảnh báo)**: thông báo trước các tình huống nguy hiểm hoặc điều kiện đặc biệt có thể xảy ra trên đường.

**Biển chỉ dẫn**: cung cấp thông tin hướng dẫn, giúp người điều khiển phương tiện di chuyển thuận lợi và an toàn.

**Biển hiệu lệnh**: thể hiện các yêu cầu bắt buộc mà người tham gia giao thông phải chấp hành, ví dụ như “đi thẳng”, “rẽ phải”, “tốc độ tối thiểu”…

**Hiển thị thông tin biển báo:**

Sau khi nhận diện thành công, hệ thống sẽ hiển thị đầy đủ thông tin liên quan đến biển báo, bao gồm:

Mã hiệu và tên biển báo theo quy chuẩn Việt Nam (TCVN 41:2019).

Nội dung, ý nghĩa và phạm vi áp dụng cụ thể của từng biển báo.

Hình ảnh minh họa trực quan, giúp người dùng dễ dàng nhận biết và ghi nhớ.

Cảnh báo mức xử phạt với biển báo đó (nếu có), theo Luật Giao thông đường bộ Việt Nam và Nghị định 100/2019/NĐ-CP cùng các văn bản sửa đổi, bổ sung.

Ví dụ: khi người dùng vi phạm biển “Cấm vượt”, “Hạn chế tốc độ”, hoặc “Cấm rẽ trái”, hệ thống sẽ tự động hiển thị mức phạt tiền và hình thức xử lý tương ứng theo:

**Tra cứu:**

Hệ thống còn có chức năng tra cứu biển báo, cho phép người dùng:

Tìm kiếm nhanh các loại biển báo theo tên, mã hoặc nhóm chức năng (cấm, nguy hiểm, chỉ dẫn, hiệu lệnh). Và cho người dùng biết các thông tin chi tiết về biển báo đó.

# PHẦN 2: GIỚI THIỆU MÔ HÌNH CNN VÀ QUY TRÌNH TRIỂN KHAI NHẬN DIỆN BIỂN BÁO GIAO THÔNG

## 2.1. Giới thiệu về mô hình CNN

### 2.1.1. Khái niệm mô hình

**CNN (Convolutional Neural Network)** là một loại mạng nơ-ron nhân tạo được ứng dụng phổ biến trong lĩnh vực **Học sâu (Deep Learning)**, đặc biệt là trong **Thị giác máy tính (Computer Vision)**. Mạng CNN có khả năng tự động trích xuất và học các đặc trưng của hình ảnh, nhờ đó được sử dụng rộng rãi trong các bài toán như nhận diện và phân loại ảnh, nhận diện khuôn mặt, phát hiện đối tượng, cùng nhiều ứng dụng khác trong công nghệ và các lĩnh vực liên quan.

### 2.1.2. Các lớp chính trong mô hình

**Lớp tích chập (Convolutional Layer):** Sử dụng các bộ lọc để trích xuất đặc trưng cục bộ từ ảnh, tạo bản đồ đặc trưng (feature maps) và giảm số lượng tham số nhờ chia sẻ trọng số..

**Lớp phi tuyến (ReLU Layer):** Áp dụng hàm kích hoạt phi tuyến giúp mạng học các đặc trưng phức tạp hơn.

**Lớp tổng hợp** (**Pooling Layer**)**:** Giảm kích thước bản đồ đặc trưng bằng cách chọn giá trị đại diện, giúp giảm độ phức tạp và tính toán.

**Lớp phẳng hóa (Flatten Layer):** Chuyển các bản đồ đặc trưng 2D thành vector 1D để đưa vào lớp phân loại.

**Lớp đầy đủ kết nối (Fully Connected Layer):** Phân loại các đặc trưng đã trích xuất thành nhãn đầu ra.

## 2.2. Ứng dụng mô hình CNN trong nhận diện biển báo giao thông

### 2.2.1. Chuẩn bị dữ liệu và tiền xử lý dữ liệu

#### 2.2.1.1. Chuẩn bị dữ liệu

Trước khi tiến hành huấn luyện mô hình, bước đầu tiên của đề tài là xây dựng tập dữ liệu các loại biển báo giao thông Việt Nam. Nhằm đảm bảo mô hình học được đặc trưng chính xác và đa dạng, toàn bộ dữ liệu sẽ được nhóm tự thu thập và tổ chức thủ công thay vì sử dụng các bộ dữ liệu có sẵn trên Internet.

Trước hết, nhóm tiến hành soạn danh sách các loại biển báo cần nhận diện, bao gồm tên, mã số và loại biển báo (biển cấm, biển nguy hiểm, biển chỉ dẫn, biển hiệu lệnh). Danh sách này được lưu trong một file **Excel** (.csv) với các cột thông tin cơ bản. Sau đó nhóm sẽ tạo các thư mục tương ứng với mỗi loại biển báo, giúp việc lưu trữ và huấn luyện mô hình trở nên thuận tiện và có hệ thống. Dựa vào các thông tin trên mạng nhóm tổng hợp được 217 biển, bao gồm (biển cấm, biển nguy hiểm, biển chỉ dẫn, biển hiệu lệnh).

Tiếp theo, để thu thập hình ảnh cho từng loại biển báo, nhóm sử dụng ba phương pháp chính nhằm đảm bảo tính phong phú và đa dạng cho tập dữ liệu:

**Ảnh chụp thực tế:** Thu thập bằng điện thoại tại các tuyến đường, khu vực giao thông khác nhau. Dữ liệu này phản ánh môi trường thật, với điều kiện ánh sáng, góc chụp và thời tiết khác nhau, giúp mô hình có khả năng nhận diện tốt hơn trong thực tế.

![](data:image/png;base64...)

Hình 2.1. Ảnh chụp thực tế

**Ảnh chụp từ Google Maps (Street View):** Sử dụng chế độ xem phố để tìm kiếm và chụp lại hình ảnh biển báo trong nhiều khu vực khác nhau. Phương pháp này giúp mở rộng phạm vi thu thập dữ liệu mà không cần di chuyển trực tiếp.

![](data:image/png;base64...)

Hình 2.2. Hình chụp từ GoogleMaps

**Ảnh mô phỏng bằng Blender:** Để đảm bảo tính đa dạng của ảnh, nhóm sử dụng phần mềm Blender để dựng các mô hình 3D của các loại biển báo dựa trên kích thước và màu sắc chuẩn theo thực tế. Sau đó, nhóm tiến hành chụp lại các góc nhìn khác nhau, tạo thành dữ liệu để huấn luyện.

![](data:image/png;base64...)

Hình 2.3. Dựng biển báo trong Blender

#### 2.2.1.2. Tiền xử lý dữ liệu

Sau khi hoàn thành việc thu thập và sắp xếp hình ảnh các loại biển báo giao thông vào từng thư mục riêng ứng với mỗi loại biển báo, bước tiếp theo là **tiến hành tiền xử lý dữ liệu** nhằm chuẩn bị cho quá trình huấn luyện mô hình..

![](data:image/png;base64...)

Hình 2.4. Biển báo sau khi được thu thập

Đầu tiên, chương trình sử dụng thư viện TensorFlow và lớp ImageDataGenerator của Keras để thực hiện việc đọc và xử lý ảnh đầu vào. Các hình ảnh được chuẩn hóa giá trị điểm ảnh (rescale) về khoảng $[0,1]$ bằng cách chia mỗi giá trị pixel cho 255, giúp giảm sai lệch do chênh lệch cường độ sáng giữa các ảnh.

Ngoài ra, dữ liệu còn được tăng cường (data augmentation) nhằm mở rộng và đa dạng hóa tập huấn luyện. Các phép biến đổi ngẫu nhiên được áp dụng bao gồm:

Xoay ảnh **(rotation\_range = 25°)** giúp mô hình nhận diện được biển báo trong các trường hợp bị nghiêng.

**Dịch chuyển ngang và dọc (width\_shift\_range, height\_shift\_range = 0.2)** để mô phỏng vị trí biển báo thay đổi trong khung hình.

**Biến dạng cắt xiên (shear\_range = 0.15)** giúp tăng khả năng nhận dạng khi biển bị chụp lệch góc.

**Phóng to hoặc thu nhỏ ngẫu nhiên (zoom\_range = 0.25)** giúp mô hình thích ứng với biển báo ở các khoảng cách khác nhau.

**Thay đổi độ sáng (brightness\_range = [0.7, 1.3])** mô phỏng các điều kiện chiếu sáng khác nhau như trời nắng, râm hoặc ban đêm.

**Dịch chuyển giá trị màu (channel\_shift\_range = 20.0)** giúp mô hình bền vững hơn với sự thay đổi màu sắc do camera hoặc môi trường.

Tất cả các phép biến đổi này giúp mô hình **tăng khả năng tổng quát (generalization)**, giảm hiện tượng **overfitting**, và có thể nhận diện tốt hơn trong các điều kiện thực tế.

Cuối cùng tập dữ liệu được chia thành hai phần: **80%** cho tập huấn luyện (training set) và **20%** cho tập kiểm thử (validation set).

![](data:image/png;base64...)

Hình 2.5. Quá trình xử lý dữ liệu

Sau khi cấu hình các bước tiền xử lý, chương trình sử dụng phương thức **flow\_from\_directory()** của lớp **ImageDataGenerato**r để nạp dữ liệu vào mô hình huấn luyện. Phương thức này cho phép tự động gán nhãn (label) cho từng ảnh dựa trên tên thư mục chứa ảnh, nghĩa là mỗi thư mục con trong tập dữ liệu tương ứng với một loại biển báo giao thông khác nhau.

**train\_generator:** dùng để cung cấp dữ liệu cho giai đoạn huấn luyện (training set), với tham số **subset="training"** và tùy chọn **shuffle=True** để xáo trộn dữ liệu ngẫu nhiên, giúp mô hình học tốt hơn và tránh ghi nhớ thứ tự mẫu.

**val\_generator:** dùng cho giai đoạn kiểm thử **(validation set),** với **subset="validation"** **và shuffle=False** để đảm bảo dữ liệu đánh giá được sử dụng cố định và ổn định trong suốt quá trình huấn luyện.

Tất cả hình ảnh được **resize** về kích thước 224x224 pixel nhằm đảm bảo tương thích với kiến trúc **MobileNetV2** được sử dụng ở các bước sau.

![](data:image/png;base64...)

Hình 2.6. Phân loại và Resize ảnh

Quy trình tiền xử lý này giúp đảm bảo dữ liệu đầu vào có tính nhất quán, giảm nhiễu, đồng thời tăng tính đa dạng của tập huấn luyện. Nhờ đó, mô hình học hiệu quả hơn và đạt độ chính xác cao hơn trong việc nhận diện các loại biển báo giao thông khác nhau.

### 2.2.2. Trích xuất đặc trưng

**Chuẩn bị thông tin đặc trưng:**

Trong quá trình xây dựng hệ thống nhận diện và cảnh báo biển báo giao thông, việc trích xuất và chuẩn bị thông tin đặc trưng cho từng loại biển báo đóng vai trò quan trọng. Sau khi mô hình CNN xử lý ảnh và đưa ra kết quả dự đoán, đầu ra của mô hình là chỉ số lớp **(class index)** tương ứng với loại biển báo nhận diện được.

Để chuyển đổi chỉ số này thành mã biển báo thực tế (ví dụ: P.101, P.102, …), hệ thống sử dụng file **label\_mapping.json**, trong đó ánh xạ giữa chỉ số và mã biển báo được lưu dưới dạng: {"0": "DP.133", "1": "DP.134",…}.

Sau khi xác định được mã biển báo, hệ thống tiếp tục truy xuất dữ liệu mô tả từ file (.csv), nơi chứa các thông tin đặc trưng tương ứng của từng biển như **hình 9.**

![](data:image/png;base64...)

Hình 2.7. Thông tin đặc trưng của biển báo

### 2.2.3. Huấn luyện mô hình

Sau khi hoàn tất quá trình tiền xử lý và chuẩn bị dữ liệu, hệ thống bắt đầu giai đoạn huấn luyện mô hình nhận diện biển báo giao thông. Trong đề tài này, nhóm sử dụng kiến trúc **MobileNetV2** thuộc họ mạng nơ-ron tích chập (CNN) làm mô hình nền (base model). MobileNetV2 được chọn vì có cấu trúc gọn nhẹ, tốc độ huấn luyện nhanh và vẫn đảm bảo độ chính xác cao.

Đầu tiên, mô hình **MobileNetV2** được tải với trọng số **pretrained** từ tập dữ liệu **ImageNet**, giúp mô hình kế thừa sẵn các đặc trưng cơ bản của hình ảnh như đường viền, màu sắc và hình khối. Phần đầu ra gốc của mạng (tham số **include\_top=False**) được loại bỏ, cho phép mô hình thích ứng với bài toán nhận diện biển báo giao thông.

Để cân bằng giữa khả năng học mới và tốc độ huấn luyện, chỉ 40 lớp cuối cùng của mạng được mở khóa **(trainable=True)**, trong khi các lớp còn lại được cố định, giúp tránh hiện tượng quá khớp **overfitting** và rút ngắn thời gian huấn luyện.

Trên nền **MobileNetV2**, nhóm thêm các lớp xử lý đặc trưng mới bằng cách sử dụng **Keras Sequential API**, bao gồm:

**Lớp GlobalAveragePooling2D**: chuyển đổi ma trận đặc trưng thành vector đặc trưng duy nhất, giảm số lượng tham số.

**Lớp Dropout(0.7) và Dropout(0.6)**: loại bỏ ngẫu nhiên các kết nối trong quá trình học, giúp tăng khả năng tổng quát hóa.

**Lớp Dense(128, activation="relu")**: trích chọn và học các đặc trưng phi tuyến.

**Lớp Dense(num\_classes, activation="softmax")**: thực hiện phân loại hình ảnh vào từng nhóm biển báo tương ứng.

Mô hình được **biên dịch (compile)** với bộ tối ưu **Adam** (learning rate ban đầu = 1e-4), hàm mất mát là **categorical\_crossentropy** và chỉ số đánh giá là **accuracy**.

Trong quá trình huấn luyện, hai cơ chế **callback** được áp dụng:

**EarlyStopping**: dừng sớm quá trình huấn luyện khi giá trị **val\_loss** không còn giảm, giúp tránh overfitting.

**ReduceLROnPlateau**: tự động giảm tốc độ học (learning rate) khi quá trình tối ưu chững lại.

![](data:image/png;base64...)

Hình 2.8. Huấn luyện mô hình

Sau khi kết thúc, mô hình được lưu lại dưới dạng tệp có định dạng (.h5), phục vụ cho giai đoạn triển khai trên hệ thống web ứng dụng Flask ở các phần sau.

# PHẦN 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ

## 3.1. Giới thiệu về các công nghệ sử dụng trong đề tài

### 3.1.1. Các công cụ hỗ trợ

**Python:** được sử dụng làm ngôn ngữ chính trong đề tài nhờ cú pháp đơn giản, dễ đọc và khả năng tích hợp mạnh với các thư viện học sâu như TensorFlow và Keras. Python được nhóm sử dụng trong phần backend cũng như việc xây dựng, huấn luyện và kiểm thử mô hình CNN nhận diện biển báo giao thông.

**JavaScript, HTML và CSS**: được nhóm dùng để phát triển giao diện web, giúp hệ thống hiển thị kết quả nhận diện một cách trực quan và thân thiện với người dùng.

**Blender**: hỗ trợ mô phỏng và tạo hình ảnh 3D của các biển báo giao thông, góp phần mở rộng và đa dạng hóa bộ dữ liệu phục vụ huấn luyện mô hình.

### 3.1.2. Các thư viện hỗ trợ

**TensorFlow:** nền tảng mã nguồn mở do Google phát triển, đóng vai trò chính trong việc xây dựng, huấn luyện và triển khai mô hình học sâu (Deep Learning).

**Keras:** thư viện tích hợp trong TensorFlow, cung cấp giao diện lập trình thuận tiện cho việc thiết kế và huấn luyện mạng nơ-ron tích chập (CNN).

**MobileNetV2:** kiến trúc CNN tối ưu cho thiết bị có tài nguyên hạn chế, được sử dụng làm mô hình nền (base model) cho bài toán phân loại biển báo.

**ImageDataGenerator:** hỗ trợ đọc, chuẩn hóa và tăng cường dữ liệu hình ảnh nhằm cải thiện khả năng tổng quát của mô hình.

**Callbacks (EarlyStopping, ReduceLROnPlateau):** giúp tối ưu quá trình huấn luyện và hạn chế hiện tượng quá khớp (overfitting).

**NumPy và Pandas:** hỗ trợ xử lý, phân tích dữ liệu dạng mảng và bảng trong quá trình huấn luyện và đánh giá.

**Matplotlib:** được sử dụng để trực quan hóa kết quả huấn luyện mô hình thông qua các biểu đồ độ chính xác (accuracy) và hàm mất mát (loss) theo từng epoch, giúp theo dõi và đánh giá hiệu quả của quá trình học.

**Flask và Flask-CORS:** được sử dụng để xây dựng API và hỗ trợ giao tiếp giữa mô hình học máy và giao diện web.

**OS và JSON:** phục vụ thao tác với hệ thống tệp và quản lý dữ liệu nhãn, đảm bảo tính linh hoạt trong lưu trữ và triển khai mô hình.

**Boostrap:** Framework mã nguồn mở hỗ trợ thiết kế giao diện web hiện đại, responsive và đồng nhất, cung cấp sẵn nhiều thành phần CSS và JavaScript tiện dụng.

**Font Awesome:** Thư viện biểu tượng mã nguồn mở chứa hàng nghìn icon vector, dễ dàng tùy chỉnh và tích hợp vào giao diện web để tăng tính trực quan và thẩm mỹ.

## 3.2. Phân tích hệ thống xử lý

Biểu đồ UseCase

![](data:image/png;base64...)

Hình 3.1. Biểu đô UseCase tổng quát

Biểu đồ Use Case thể hiện các chức năng chính của hệ thống nhận diện biển báo giao thông và cảnh báo mức xử phạt, tập trung vào người dùng. Hệ thống gồm hai phần chính:

**Trang chủ:** Tập hợp các biển báo giao thông theo nhóm (cấm, nguy hiểm, chỉ dẫn, hiệu lệnh). Người dùng có thể tìm kiếm biển báo theo tên hoặc mã số và xem chi tiết gồm ý nghĩa, phạm vi áp dụng và mức xử phạt.

**Trang SignAI:** Cho phép người dùng tải ảnh biển báo lên, mô hình CNN sẽ nhận diện và hiển thị thông tin tương tự trang chi tiết

## 3.3. Triển khai/ Sử dụng hệ thống

### 3.3.1. Chuẩn bị các tệp dữ liệu

Trước khi chạy hệ thống, ta cần kiểm tra các tệp mô hình và dữ liệu hỗ trợ đã được đặt đúng vị trí và tên như trong mã nguồn.

Với **MODEL\_PATH** là đường dẫn đến tệp mô hình học sâu đã huấn luyện.

Tiếp theo **LABEL\_PATH** là tệp chứa ánh xạ giữa chỉ số lớp và mã biển báo giao thông.

Cuối cùng **CSV\_PATH** là tệp chứa thông tin chi tiết về từng loại biển báo (tên biển, loại biển, thông tin tóm tắt của biển), ví dụ:

![](data:image/png;base64...)

Hình 3.2. Các tệp dữ liệu cần thiết

### 3.3.2. Khởi chạy ứng dụng

Sau khi đã chuẩn bị đầy đủ các tệp cần thiết (mô hình đã huấn luyện, tệp nhãn phân loại, và dữ liệu mô tả), hệ thống được khởi chạy thông qua hai thành phần chính:

Khởi chạy backend **(Flask).** Tại thư mục chứa tệp “app.py” ta chạy lệnh **python app.py.** Flask sẽ khởi chạy tại địa chỉ mặc định: **http://127.0.0.1:5000/.**

Về phần frontend, mở tệp **dash.html** và dùng tính năng **Go Live** của VS Code dể chạy giao diện. Trang chủ của hệ thống sẽ hiển thị danh sách các biển báo cùng thông tin chi tiết tương ứng.

Ngoài ra, người dùng có thể truy cập trang “Nhận diện biển báo” để tải ảnh lên và xem kết quả dự đoán từ mô hình CNN đã được huấn luyện.

### 3.3.3. Dự đoán biển báo với mô hình đã lưu

Sau khi quá trình huấn luyện hoàn tất, mô hình học sâu được lưu lại dưới dạng tệp **(model\_phan\_loai\_bien\_bao\_1.h5)** cùng với tệp ánh xạ **(label\_mapping.json).** Bước tiếp theo là **tải mô hình đã huấn luyện** và **thực hiện dự đoán trên ảnh mới**. Chương trình sẽ nạp lại mô hình đã huấn luyện bằng **tf.keras.models.load\_model().** Tiếp theo, ảnh đàu vào được đưa qua mô hìn bằng **model.predict(x)** để nhận về một mảng xác suất (phần trăm dự đoán của biển báo).

Từ mảng này, chương trình xác định chỉ số của lớp có xác suất cao nhất bằng **np.argmax(preds)** và lưu vào biến **pred\_idx**. Chỉ số này sau đó được chuyển đổi thành mã biển báo tương ứng (ví dụ "P.103a") thông qua tệp **label\_mapping.json.**

Cuối cùng, khi đã xác định được mã biển báo, chương trình sử dụng hàm **get\_info\_from\_code()** để tra cứu thông tin chi tiết được lưu trong tiệp (.csv). Ta sẽ có được một đối tượng **result** chứa đầy đủ thông tin gồm: “mã, tên biển, loại biển, mô tả tóm tắt và mức độ tin cậy”.

![](data:image/png;base64...)

Hình 3.3. Nhận diện biển báo

![](data:image/png;base64...)

Hình 3.4. Kết quả khi nhận diện biển báo

## 3.4. Đánh giá kết quả thực nghiệm

Sau khi tiến hành chạy thử nghiệm hệ thống, nhóm thu được kết quả như sau:

|  |  |
| --- | --- |
| Mã biển báo | Kết quả dự đoán biển báo |
| P.106b và I.418 | ![](data:image/png;base64...)![](data:image/png;base64...) |

*Bảng* 3.*1*. Kết quả dự đoán trên một số biển báo

Từ biểu đồ **hình 3.5**, ta thấy:

Độ chính xác trên tập huấn luyện **(Train Accuracy)** tăng dần theo số epoch, cho thấy mô hình học được đặc trưng của dữ liệu.

Độ chính xác trên tập kiểm định **(Validation Accuracy)** đạt mức cao (~85–90%) và ổn định sau khoảng 20 epoch, chứng tỏ mô hình có khả năng tổng quát hóa tốt.

Độ chênh lệch nhỏ giữa hai đường cho thấy hiện tượng overfitting không đáng kể, chứng minh mô hình được huấn luyện hiệu quả.

![](data:image/png;base64...)

Hình 3.5. Biểu đồ độ chính xác huấn luyện và kiểm định của mô hình

Từ biểu đồ **hình 3.6**, ta thấy:

Giá trị **Train Loss** và **Validation Loss** đều giảm rõ rệt qua từng epoch, chứng tỏ mô hình học được các đặc trưng quan trọng từ dữ liệu.

Đường **Validation Loss** có giá trị tương đồng hoặc thấp hơn so với **Train Loss**, điều này cho thấy mô hình không bị overfitting và có khả năng tổng quát hóa tốt trên dữ liệu chưa thấy.

![](data:image/png;base64...)

Hình 3.6. Biểu đồ hàm mất mát trên tập huấn luyện và kiểm định của mô hình

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Epochs | Loss | Accuracy | Val\_loss | Val\_accuracy |
| 1 | 5.5002 | 0.0037 | 5.3585 | 0.0052 |
| 10 | 2.8100 | 0.2847 | 1.8099 | 0.5052 |
| 20 | 1.1778 | 0.6244 | 0.6862 | 0.7648 |
| 30 | 0.6768 | 0.7705 | 0.4161 | 0.8620 |

Bảng 3.2. So sánh giá trị các epochs

**Kết luận chung:**

Từ những hình ảnh và bảng biểu trên, mô hình CNN được huấn luyện hiệu quả, vừa đạt độ chính xác cao, vừa có khả năng tổng quát hóa tốt trên các dữ liệu biển báo. Quá trình học ổn định, không gặp hiện tượng overfitting quá nghiêm trọng.

# KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

Sau quá trình tìm hiểu và xây dựng hệ thống nhận diện biển báo giao thông bằng mô hình CNN, nhóm chúng em đã có cơ hội tiếp cận sâu hơn với các công nghệ học sâu (Deep Learning) và ứng dụng thực tế của trí tuệ nhân tạo trong lĩnh vực giao thông thông minh. Đề tài không chỉ giúp nhóm hiểu rõ hơn về quy trình huấn luyện và triển khai mô hình CNN mà còn rút ra được nhiều kinh nghiệm về tiền xử lý dữ liệu, thiết kế giao diện người dùng và kết nối giữa các thành phần của hệ thống.

**Kết quả đạt được:**

Hệ thống nhận diện biển báo hoạt động ổn định, mô hình CNN được huấn luyện thành công và có khả năng phân loại chính xác các loại biển báo cơ bản theo quy chuẩn Việt Nam, bao gồm: biển cấm, biển cảnh báo nguy hiểm, biển chỉ dẫn và biển hiệu lệnh.

Giao diện đơn giản, dễ sử dụng, giúp người dùng có thể tải lên ảnh biển báo, nhận kết quả nhận diện cũng như xem thông tin và mức xử phạt tương ứng.

Dữ liệu huấn luyện đa dạng và được xử lý hợp lý, bao gồm cả hình ảnh dựng từ Blender và ảnh thực tế, giúp mô hình học được nhiều đặc trưng khác nhau của biển báo trong các điều kiện ánh sáng và góc nhìn khác nhau.

Khả năng mở rộng tốt, hệ thống được thiết kế linh hoạt, có thể dễ dàng bổ sung thêm loại biển báo mới hoặc tích hợp với các công nghệ AI khác như YOLO cho nhận diện biển báo theo video.

**Những điều còn hạn chế:**

Độ chính xác của mô hình trong một số trường hợp chưa cao, đặc biệt khi biển báo bị mờ, nghiêng hoặc có vật cản.

Dữ liệu về các loại biển báo chưa được nhiều nên khi training có overfitting nhẹ. Ngoài ra còn chưa bao quát hết tất cả các loại biển báo theo quy chuẩn Việt Nam.

Tốc độ xử lý còn phụ thuộc vào cấu hình máy, nên khi chạy trên thiết bị cấu hình yếu, thời gian nhận diện có thể chậm.

**Hướng phát triển trong tương lai:**

Nếu mở rộng được hơn về tệp dữ liệu thì nhóm sẽ thử nghiệm các kiến trúc mạng tiên tiến hơn như ResNet, EfficientNet hoặc Vision Transformer.

Phát triển tính năng nhận diện video theo thời gian thực bằng cách kết hợp mô hình YOLO hoặc MobileNet SSD, giúp hệ thống có thể nhận diện biển báo trực tiếp từ camera hoặc video giám sát.

Xây dựng phiên bản ứng dụng di động (mobile app) để người dùng có thể sử dụng trực tiếp trên điện thoại, thuận tiện trong việc tra cứu và nhận diện biển báo ngoài thực tế.

Tối ưu hóa giao diện người dùng, bổ sung chức năng lưu lịch sử nhận diện biển báo và gợi ý biển báo tương tự nhằm tăng trải nghiệm sử dụng.

**Kết luận:**

Qua quá trình thực hiện đề tài, nhóm chúng em đã hiểu rõ hơn về ứng dụng của trí tuệ nhân tạo và học sâu trong thực tế, đặc biệt là quá trình xử lý và huấn luyện mô hình CNN. Do kiến thức và kinh nghiệm còn hạn chế, bài làm của nhóm vẫn còn nhiều thiếu sót, chúng em rất mong nhận được góp ý từ cô để đề tài có thể hoàn thiện và phát triển tốt hơn trong tương lai. Nhóm chúng em xin chân thành cảm ơn cô giáo đã hướng dẫn và hỗ trợ trong suốt quá trình thực hiện đề tài.

# TÀI LIỆU THAM KHẢO

1. GS. TS Từ Minh Phương, *Giáo trình Nhập môn Trí tuệ nhân tạo, Học viện CN BCVT, 2020*
2. https://viblo.asia/p/deep-learning-tim-hieu-ve-mang-tich-chap-cnn-maGK73bOKj2
3. https://www.youtube.com/watch?v=rmNTqYGpr6Y&t=362s
4. https://vi.wikipedia.org/wiki/Bi%E1%BB%83n\_b%C3%A1o\_giao\_th%C3%B4ng\_t%E1%BA%A1i\_Vi%E1%BB%87t\_Nam
5. https://cdn.thuvienphapluat.vn/phap-luat/2022-2/CTNN/quy-chuan-ky-thuat-qcvn-41-2019-bgtvt-bao-hieu-duong-bo.pdf
6. https://thuvienphapluat.vn/iThong/tra-cuu-xu-phat-giao-thong.aspx

# BẢNG PHÂN CHIA CÔNG VIỆC

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| STT | Họ và tên | Tiêu đề | Nội dung đề mục | Đánh giá |
| 1 | Bùi Quang Khải | 1.3.1 | Khái niệm về thị giác máy tính | 18% |
| 1.3.2 | Các bài toán cơ bản trong Thị giác máy tính |
| 3.1.1 | Các công cụ hỗ trợ |
| 3.3.1 | Chuẩn bị các tệp dữ liệu |
| 3.4 | Đánh giá kết quả thực nghiệm |
| # | Code giao diện |
| # | Thu thập data |
| 2 | Nguyễn Hoàng Anh | 1.2.1 | Khái niệm về trí tuệ nhân tạo | 22% |
| 1.3.3 | Ứng dụng của Thị giác máy tính |
| 2.2.1.2 | Tiền xử lý dữ liệu |
| 2.2.3 | Huấn luyện mô hình |
| # | Thu thập data |
| # | Train mô hình |
| 3 | Bùi Kim Đạt | 1.1 | Giới thiệu về công ty | 18% |
| 1.1.2 | Tổng quan về dự án công ty |
| 1.1.3 | Giới thiệu về dự án thực tập |
| 3.3.2 | Khởi chạy ứng dụng |
| # | Thu thập data |
| # | Backend code |
| 4 | Âu Xuân Mạnh | 1.2.2 | Các hướng nghiên cứu trí tuệ nhân tạo | 20% |
| 2.1.1 | Khái niệm mô hình |
| 3.1.2 | Các thư viện hỗ trợ |
| 3.3.3 | Dự đoán biển báo với mô hình đã lưu |
| # | Thu thập data |
| # | Backend code |
| 5 | Trương Thành Nam | 1.2.3 | Phân loại trí tuệ nhân tạo | 22% |
| 2.1.2 | Các lớp chính trong mô hình |
| 2.2.1.1 | Chuẩn bị dữ liệu |
| 3.2.1 | Biểu đồ UseCase |
| # | Thu thập data |
| # | Train mô hình |