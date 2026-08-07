TRƯỜNG ĐẠI HỌC KIẾN TRÚC HÀ NỘI
KHOA CÔNG NGHỆ THÔNG TIN
-----o0o-----
BÁO CÁO THỰC TẬP TỐT NGHIỆP
Tên đề tài:
Thiết kế và phát triển giao diện người dùng cho ứng dụng web bán
quần áo nữ sử dụng ReactJS.
GIÁO VIÊN HƯỚNG DẪN : THS. PHẠM THỊ THANH MAI
SINH VIÊN THỰC HIỆN : NGUYỄN THỊ QUỲNH GIANG
LỚP : 21CN2
HÀ NỘI 09-2025

LỜI NÓI ĐẦU
Trong bối cảnh công nghệ thông tin và Internet ngày càng phát triển mạnh mẽ,
thương mại điện tử đã trở thành một trong những lĩnh vực có tốc độ tăng trưởng nhanh
và đóng vai trò quan trọng trong đời sống hiện đại. Việc thiết kế và phát triển giao diện
người dùng (UI) cho các ứng dụng web không chỉ mang lại sự tiện lợi cho khách hàng
mà còn góp phần nâng cao năng lực cạnh tranh của doanh nghiệp. Đặc biệt, trong ngành
thời trang – nơi luôn đòi hỏi sự sáng tạo, tính thẩm mỹ và sự đổi mới liên tục – một giao
diện web hiện đại, thân thiện và dễ sử dụng chính là yếu tố then chốt để thu hút và giữ
chân khách hàng.
Xuất phát từ nhu cầu thực tiễn đó, em đã lựa chọn đề tài: “Thiết kế và phát triển giao
diện người dùng cho ứng dụng web bán quần áo nữ sử dụng ReactJS”. Thông qua đề tài
này, em mong muốn vận dụng những kiến thức đã học vào thực tế, đồng thời tìm hiểu
sâu hơn về cách xây dựng giao diện người dùng hiện đại, tối ưu hiệu suất và phù hợp
với xu hướng thương mại điện tử hiện nay.
Trong quá trình thực tập và thực hiện báo cáo, em đã có cơ hội tiếp cận môi trường
làm việc thực tế, rèn luyện kỹ năng phân tích, thiết kế và phát triển phần mềm. Bên cạnh
đó, em nhận được sự hỗ trợ, định hướng và chỉ dẫn tận tình từ cô ThS. Phạm Thị Thanh
Mai, người đã giúp em giải đáp những khó khăn, hoàn thiện ý tưởng và triển khai nội
dung đề tài một cách khoa học và hiệu quả.
Em xin chân thành cảm ơn sự hướng dẫn của cô giáo, sự giúp đỡ của bạn bè và sự tạo
điều kiện từ nhà trường đã giúp em hoàn thành báo cáo thực tập tốt nghiệp này. Tuy đã
có nhiều cố gắng, song do thời gian và kiến thức còn hạn chế, báo cáo khó tránh khỏi
những thiếu sót. Em rất mong nhận được những ý kiến đóng góp để hoàn thiện hơn trong
các nghiên cứu và công việc sau này.
2

MỤC LỤC
LỜI NÓI ĐẦU ................................................................................................................ 2
DANH MỤC TỪ VIẾT TẮT ........................................................................................ 4
CHƯƠNG 1. TỔNG QUAN ......................................................................................... 5
1.1. GIỚI THIỆU VỀ DOANH NGHIỆP .................................................................... 5
1.2. TÓM TẮT QUÁ TRÌNH THỰC TẬP ................................................................. 5
CHƯƠNG 2. CƠ SỞ LÝ THUYẾT ............................................................................. 7
2.1. Giới thiệu về ReactJS ............................................................................................. 7
2.2. Các khái niệm cơ bản trong ReactJS .................................................................... 7
2.3. UI/UX trong ứng dụng web thương mại điện tử ................................................ 8
2.3.1. Khái niệm cơ bản về UI và UX ..................................................................... 9
2.3.2. Các Yếu tố UX then chốt cho Website TMĐT ............................................. 9
2.3.3. Yêu cầu UI đặc thù cho Website ................................................................. 10
CHƯƠNG 3. NỘI DUNG THỰC TẬP ..................................................................... 12
3.1. Tìm hiểu công nghệ và cài đặt môi trường......................................................... 12
3.2. Quy trình thiết kế và phát triển giao diện .......................................................... 14
3.2.1. Phân tích yêu cầu ......................................................................................... 14
3.2.2. Thiết kế giao diện (UI/UX) ......................................................................... 15
3.2.3. Xây dựng cấu trúc thư mục dự án ............................................................... 15
3.2.4. Phân tích và thiết kế giao diện ..................................................................... 16
3.2.5. Phát triển từng chức năng ............................................................................ 17
3.3. Các chức năng chính đã thực hiện ...................................................................... 18
3.4. Đánh giá kết quả đạt được ................................................................................... 21
CHƯƠNG 4. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN ......................................... 23
4.1. Kết quả đạt được .................................................................................................. 23
4.2. Hạn chế và khó khăn ............................................................................................ 23
4.3. Hướng phát triển trong tương lai ....................................................................... 23
TÀI LIỆU THAM KHẢO ........................................................................................... 25
3

DANH MỤC TỪ VIẾT TẮT
| Từ viết tắt  |                 | Giải thích  |                                          | Ý nghĩa  |
| ------------ | --------------- | ----------- | ---------------------------------------- | -------- |
| UI           | User Interface  |             | Giao diện người dùng — phần hiển thị mà  |          |
người dùng tương tác trực tiếp
| UX  | User Experience  |     | Trải nghiệm người dùng — tổng thể cảm  |     |
| --- | ---------------- | --- | -------------------------------------- | --- |
nhận khi sử dụng sản phẩm
| TMĐT  | Thương mại điện tử  |     | Hoạt động kinh doanh qua internet  |     |
| ----- | ------------------- | --- | ---------------------------------- | --- |
| COD   | Cash On Delivery    |     | Thanh toán khi nhận hàng           |     |
| SKU   | Stock Keeping Unit  |     | Mã quản lý hàng hóa riêng biệt     |     |
JSX  JavaScript XML  Cú pháp mở rộng dùng trong React để viết
HTML trong JavaScript
| npm  | Node Package  |     | Trình quản lý gói cho Node.js  |     |
| ---- | ------------- | --- | ------------------------------ | --- |
Manager
| Vite  |     |     | Công cụ khởi tạo dự án front-end nhanh  |     |
| ----- | --- | --- | --------------------------------------- | --- |
HTML  HyperText  Markup  Ngôn ngữ đánh dấu siêu văn bản dùng để
|      | Language                |     | tạo cấu trúc website            |     |
| ---- | ----------------------- | --- | ------------------------------- | --- |
| CSS  | Cascading Style Sheets  |     | Ngôn ngữ định kiểu cho website  |     |
JSON  JavaScript  Object  Định dạng dữ liệu dễ đọc cho người và máy
Notation

  4

CHƯƠNG 1. TỔNG QUAN
1.1. GIỚI THIỆU VỀ DOANH NGHIỆP
Công Ty TNHH Công Nghệ và Dịch Vụ Tin Học An Bình, thành lập ngày
18/10/2010, có trụ sở tại 124 phố Ngô Quyền, Quận Hà Đông, Thành phố Hà Nội. Với
hơn một thập kỷ hoạt động trong lĩnh vực công nghệ thông tin, An Bình luôn hướng tới
mục tiêu cung cấp các giải pháp công nghệ hiện đại cùng dịch vụ tin học chất lượng cao,
đáp ứng nhu cầu ngày càng đa dạng của khách hàng.
Trải qua quá trình phát triển, An Bình đã xây dựng uy tín vững chắc nhờ kinh
nghiệm chuyên sâu, đội ngũ nhân sự giàu năng lực và phương châm phục vụ tận tâm.
Hiện nay, công ty tập trung triển khai và phát triển các dịch vụ trọng tâm như:
Tư vấn và triển khai giải pháp công nghệ thông tin
Cung cấp các giải pháp CNTT tối ưu cho doanh nghiệp, bao gồm hệ thống mạng, hạ
tầng máy chủ, và giải pháp lưu trữ dữ liệu, nhằm nâng cao hiệu quả vận hành và tiết
kiệm chi phí.
Phát triển phần mềm theo yêu cầu
Xây dựng phần mềm quản lý, ứng dụng doanh nghiệp, và các giải pháp số hóa quy trình
nghiệp vụ, đáp ứng đặc thù ngành nghề và nhu cầu riêng của từng khách hàng.
Dịch vụ bảo trì và hỗ trợ kỹ thuật
Đảm bảo hệ thống CNTT hoạt động ổn định, liên tục với dịch vụ bảo trì định kỳ, xử lý
sự cố nhanh chóng và hỗ trợ kỹ thuật 24/7.
Đào tạo và chuyển giao công nghệ
Cung cấp chương trình đào tạo chuyên sâu cho đội ngũ nhân viên doanh nghiệp, giúp
nâng cao năng lực sử dụng công nghệ và tối ưu hóa hiệu quả công việc.
Giải pháp an ninh mạng và bảo mật thông tin
Tư vấn và triển khai các biện pháp bảo mật, chống xâm nhập và bảo vệ dữ liệu quan
trọng, đảm bảo an toàn thông tin cho doanh nghiệp.
1.2. TÓM TẮT QUÁ TRÌNH THỰC TẬP
Trong thời gian thực tập từ ngày 01/09/2025 đến ngày 28/09/2025 tại Công ty
TNHH Công nghệ và Dịch vụ Tin học An Bình, em đã thực hiện các công việc theo kế
hoạch đã đề ra:
5

Tuần 1 (01/09 – 07/09): Tìm hiểu ReactJS và các khái niệm cơ bản như component,
props, state, hooks, lifecycle. Đồng thời nghiên cứu đặc thù của các website thương mại
điện tử trong lĩnh vực thời trang nữ để xác định các thành phần giao diện cần thiết.
Tuần 2 (08/09 – 14/09): Cài đặt môi trường phát triển bao gồm Node.js, npm,
Visual Studio Code; khởi tạo dự án ReactJS với Vite; xây dựng cấu trúc thư mục và
chuẩn bị các thư viện hỗ trợ.
Tuần 3 (15/09 – 21/09): Bắt đầu phát triển giao diện người dùng: thiết kế và triển
khai các component chính; hoàn thiện trang chủ, trang danh mục sản phẩm, trang chi
tiết sản phẩm theo nguyên tắc UI/UX.
Tuần 4 (22/09 – 28/09): Hoàn thiện các chức năng còn lại như giỏ hàng, thanh
toán, tìm kiếm và lọc sản phẩm. Kiểm thử giao diện, tối ưu trải nghiệm người dùng,
đồng thời viết báo cáo tổng hợp kết quả thực tập.
Kết quả, em đã hoàn thành đúng tiến độ và đạt được mục tiêu đề ra: xây dựng giao
diện cơ bản cho ứng dụng web thương mại điện tử quần áo nữ bằng ReactJS, đáp ứng
các yêu cầu về thẩm mỹ, tính tiện dụng và tính responsive.
6

CHƯƠNG 2. CƠ SỞ LÝ THUYẾT
2.1. Giới thiệu về ReactJS
React (hoặc ReactJS) là một thư viện JavaScript mã nguồn mở do Meta (Facebook)
phát triển để xây dựng giao diện người dùng (UI) cho các ứng dụng web. Nó cho phép
tạo các thành phần UI có thể tái sử dụng, sử dụng Virtual DOM để cải thiện hiệu suất
và hỗ trợ JSX để viết mã HTML trong JavaScript, giúp xây dựng các ứng dụng phức tạp
một cách hiệu quả và có thể mở rộng.
Các đặc điểm cơ bản của ReactJS:
Thư viện UI: React chỉ tập trung vào lớp giao diện, giúp quản lý và cập nhật các
thành phần UI một cách hiệu quả.
Component-based: Ứng dụng được chia thành các thành phần nhỏ có thể tái sử
dụng, giúp giảm thiểu việc viết mã trùng lặp và làm cho quá trình phát triển đơn giản
hơn.
Virtual DOM: React sử dụng một bản sao ảo của DOM để tối ưu hóa việc cập
nhật giao diện, giúp tăng hiệu suất và tốc độ của ứng dụng.
JSX: Một cú pháp mở rộng của JavaScript, cho phép lập trình viên viết các thẻ
tương tự HTML ngay trong mã JavaScript, làm cho quá trình phát triển trở nên trực
quan và dễ dàng hơn.
Hiệu suất cao: Nhờ vào việc sử dụng Virtual DOM và cách tiếp cận theo thành
phần, React có thể xây dựng các ứng dụng web nhanh chóng, mượt mà và có khả năng
mở rộng cao.
2.2. Các khái niệm cơ bản trong ReactJS
2.2.1. Components
Components là khối xây dựng cơ bản của bất kì ứng dụng React nào. Chúng là các
đoạn mã độc lập, tái sử dụng được, có chức năng trả về các phần tử React (thường là
HTML) để hiển thị trên giao diện người dùng.
Phân loại :
Function Components (Thành phần hàm): Là các hàm trong JavaScript đơn giản,
nhận đối số là props và trả về các phần tử React.
Class Components (Thành phần lớp): Là các lớp JavaScript mở rộng từ
React.Component và phải có phương thức render().
7

Mục đích: Chia nhỏ giao diện người dùng thành các phần nhỏ, dễ quản lý.
2.2.2. JSX(JavaScript XML)
JSX là một cú pháp mở rộng cho JavaScript, cho phép bạn viết cấu trúc giống như
HTML ngay trong các file JavaScript của mình.
Tính năng: JSX được biên dịch thành các lệnh gọi hàm React.createElement() và
tạo ra các phần tử React.
Ví dụ:
JavaScript
const element = <h1>Xin chào, React!</h1>;
Lợi ích: Giúp việc mô tả cấu trúc UI trở nên trực quan và dễ đọc hơn.
2.2.3. Props (Properties - Thuộc tính)
Props là cơ chế để truyền dữ liệu từ Component cha xuống Component con.
Đặc điểm: Props là chỉ đọc (read-only), nghĩa là component con không thể tự ý
thay đổi giá trị của props mà nó nhận được.
Mục đích: Cấu hình và tùy chỉnh component con.
2.2.4. State (Trạng thái)
State là một đối tượng JavaScript được sử dụng để lưu trữ dữ liệu hoặc thông tin
về component mà có thể thay đổi theo thời gian
Đặc điểm: State là private và chỉ thuộc về component đang chứa nó.
Thay đổi: Khi state thay đổi, React sẽ tự động re-render (kết xuất lại) component
để cập nhật giao diện người dùng.
Sử dụng với Function Components: Dùng Hook useState().
2.2.5. Hooks
Hooks là một tính năng được giới thiệu trong React 16.8, cho phép bạn sử dụng
state và các tính năng khác của React mà không cần viết Class Components.
Các Hook quan trọng:
useState: Để thêm state vào Function Components.
useEffect: Để thực hiện các "side effects" (tác dụng phụ) như fetch dữ liệu,
subscribe sự kiện... trong Function Components.
useContext: Để truy cập dữ liệu từ React Context.
2.3. UI/UX trong ứng dụng web thương mại điện tử
8

2.3.1. Khái niệm cơ bản về UI và UX
a. Giao diện Người dùng (User Interface - UI)
UI là tập hợp các yếu tố thị giác (visual) mà người dùng tương tác trực tiếp, bao
gồm:
Thiết kế đồ họa: Màu sắc, font chữ, hình ảnh, biểu tượng.
Bố cục (Layout): Sắp xếp các thành phần trên màn hình (thanh điều hướng, giỏ
hàng, nút bấm).
Tính nhất quán: Đảm bảo thương hiệu và phong cách thiết kế được duy trì đồng
bộ trên toàn bộ trang web.
Mục tiêu: Tạo ra một giao diện đẹp mắt, dễ nhận biết và hấp dẫn thị giác.
b. Kinh nghiệm Người dùng (User Experience - UX)
UX mô tả toàn bộ cảm xúc, thái độ và nhận thức của người dùng khi tương tác với
sản phẩm hoặc dịch vụ.
Tính hữu dụng (Usability): Trang web có dễ sử dụng không? Người dùng có thể
hoàn thành mục tiêu (tìm kiếm, mua hàng) một cách nhanh chóng không?
Tính tiếp cận (Accessibility): Trang web có dễ dàng truy cập và sử dụng trên các
thiết bị khác nhau (di động, máy tính bảng, máy tính) và với các đối tượng người dùng
khác nhau không?
Hiệu suất: Tốc độ tải trang, độ phản hồi của các thao tác.
Mục tiêu: Tạo ra trải nghiệm mua sắm mượt mà, hiệu quả và đáng nhớ.
2.3.2. Các Yếu tố UX then chốt cho Website TMĐT
Thiết kế UX cho ngành thời trang cần tập trung vào việc giảm thiểu ma sát trong
quá trình mua hàng và tăng cường sự tin tưởng cũng như cảm xúc của người mua.
a. Tính Phản hồi (Responsiveness) và Mobile-First
Ưu tiên thiết bị di động: Phần lớn giao dịch TMĐT hiện nay đến từ các thiết bị di
động. Giao diện phải được thiết kế theo nguyên tắc Mobile-First, đảm bảo bố cục, hình
ảnh và nút bấm hoạt động hoàn hảo trên màn hình nhỏ.
Tốc độ tải trang: Thời trang là ngành đòi hỏi nhiều hình ảnh chất lượng cao. Cần
tối ưu hóa hình ảnh để đảm bảo tốc độ tải nhanh, tránh làm khách hàng khó chịu và rời
bỏ trang web.
b. Quy trình Mua hàng Thuận tiện (Seamless Checkout)
9

Giỏ hàng minh bạch: Hiển thị rõ ràng tổng tiền, chi phí vận chuyển, và mã giảm
giá.
Thanh toán đơn giản hóa: Hạn chế số bước thanh toán. Cho phép mua hàng không
cần đăng ký tài khoản (Guest Checkout).
Hỗ trợ đa dạng phương thức thanh toán: Thanh toán khi nhận hàng (COD), thẻ
ngân hàng, ví điện tử.
c.Hệ thống Tìm kiếm và Lọc thông minh
Tìm kiếm mạnh mẽ: Hỗ trợ tìm kiếm theo tên sản phẩm, mã SKU, và cả các từ
khóa không chính xác.
Bộ lọc chi tiết: Cần có các bộ lọc chuyên biệt cho ngành thời trang như: Kích cỡ
(Size), Màu sắc (Color), Chất liệu (Fabric), Kiểu dáng (Style), Mức giá.
2.3.3. Yêu cầu UI đặc thù cho Website
UI trong TMĐT thời trang nữ cần phải truyền tải được phong cách và tính thẩm
mỹ của thương hiệu.
a. Trình bày Sản phẩm (Product Presentation)
Hình ảnh chất lượng cao: Sử dụng ảnh rõ nét, đa góc độ, bao gồm ảnh chi tiết về
chất liệu và ảnh người mẫu mặc để khách hàng dễ dàng hình dung.
Video và ảnh 360 độ: Cung cấp trải nghiệm chân thực hơn về độ rũ, phom dáng
của sản phẩm.
Thông tin chi tiết (Detailed Information): Mô tả sản phẩm phải đầy đủ về chất liệu,
hướng dẫn giặt ủi, và bảng kích thước chuẩn kèm theo hướng dẫn đo.
b. Màu sắc và Thẩm mỹ
Phối màu hài hòa: Lựa chọn bảng màu UI phù hợp với đối tượng mục tiêu nữ giới
và phong cách thương hiệu (ví dụ: các màu nhẹ nhàng, thanh lịch hoặc tươi sáng, trẻ
trung).
Không gian trắng (Whitespace): Sử dụng không gian trắng hợp lý để làm nổi bật
sản phẩm, tạo cảm giác sang trọng, không bị rối mắt.
c. Điều hướng trực quan (Intuitive Navigation)
Menu rõ ràng: Phân loại sản phẩm theo các danh mục logic (ví dụ: Đầm, Áo, Quần,
Phụ kiện, Sản phẩm mới, Bộ sưu tập).
10

Thanh điều hướng (Header/Footer): Đảm bảo các thành phần quan trọng như Giỏ
hàng (Cart), Tài khoản (Account), Thanh tìm kiếm (Search Bar) luôn dễ dàng truy cập.
11

CHƯƠNG 3. NỘI DUNG THỰC TẬP
3.1. Tìm hiểu công nghệ và cài đặt môi trường
3.1.1. Cài đặt Node.js và npm
Để lập trình với ReactJS, môi trường Node.js là bắt buộc. Node.js cung cấp
runtime cho JavaScript và npm (Node Package Manager) để quản lý thư viện.
Các bước thực hiện:
- Truy cập trang chủ https://nodejs.org và tải bản LTS (ổn định).
- Cài đặt theo hướng dẫn, đồng thời chọn Add Node.js to PATH.
Kiểm tra cài đặt:
3.1.2. Khởi tạo project React với Vite trong Visual Studio Code
Bước 1: Mở Visual Studio Code
Nhấn Start → tìm Visual Studio Code → mở ứng dụng.
Tạo một thư mục chứa project, ví dụ: D:\ReactProjects\ecommerce-clothes.
Vào File → Open Folder trong VS Code để mở thư mục này.
12

Bước 2: Mở Terminal trong VS Code
Chọn menu View → Terminal hoặc nhấn tổ hợp phím Ctrl + `.
Lúc này, terminal của VS Code sẽ mở ngay bên dưới cửa sổ làm việc.
Bước 3: Khởi tạo project Vite + React
Trong terminal, gõ lệnh: npm create vite@latest ecommerce-clothes
VS Code sẽ hiện ra một loạt lựa chọn:
- Select a framework: React
- Select a variant: JavaScript
13

Bước 4: Chạy project
Khởi động ứng dụng: npm run dev
Terminal sẽ trả về thông báo:
VITE vX.X.X ready in XXX ms
➜ Local: http://localhost:5173/
Ấn ctrl+click vào đường dẫn http://localhost:5173/ trong terminal để mở trực tiếp
trên trình duyệt.
3.2. Quy trình thiết kế và phát triển giao diện
3.2.1. Phân tích yêu cầu
Trước khi tiến hành xây dựng giao diện, việc phân tích yêu cầu là bước quan trọng
để xác định phạm vi và mục tiêu của ứng dụng:
- Đối tượng người dùng: Nữ giới trong độ tuổi 18–35, có nhu cầu mua sắm quần
áo trực tuyến.
- Chức năng cơ bản cần có:
Trang chủ hiển thị sản phẩm nổi bật và các bộ sưu tập.
Trang danh mục sản phẩm theo từng loại (đầm, áo, quần, phụ kiện...)
Trang chi tiết sản phẩm (ảnh, mô tả, giá, size, màu sắc, đánh giá).
Chức năng giỏ hàng, thanh toán.
14

Quản lý tài khoản người dùng (đăng nhập, đăng ký).
- Yêu cầu phi chức năng:
Giao diện hiện đại, dễ sử dụng, thân thiện trên thiết bị di động (responsive design).
Tốc độ tải nhanh, tối ưu hình ảnh và dữ liệu.
Dễ dàng mở rộng và bảo trì.
3.2.2. Thiết kế giao diện (UI/UX)
Quá trình thiết kế giao diện được thực hiện trực tiếp trong quá trình lập trình bằng
ReactJS kết hợp CSS:
- Ý tưởng thiết kế: Tham khảo từ các website thương mại điện tử thời trang phổ
biến (như Shopee, Zara, Shein) để lựa chọn bố cục, màu sắc và phong cách phù hợp với
đối tượng khách hàng nữ.
- Cách triển khai UI/UX:
Phác thảo ý tưởng trên giấy: Vẽ bố cục cơ bản của các trang (trang chủ, trang danh
mục, trang sản phẩm, giỏ hàng).
Triển khai trực tiếp bằng code: Tạo component React cho từng phần giao diện và
sử dụng TailwindCSS để thử nghiệm nhanh các phong cách, màu sắc, bố cục.
Tối ưu trải nghiệm người dùng (UX): Trong quá trình code, thường xuyên chạy
thử và kiểm tra trên các thiết bị (máy tính, điện thoại) để đảm bảo giao diện responsive
và dễ thao tác.
- Nguyên tắc áp dụng:
Mobile-First: Giao diện được viết và kiểm tra trước trên màn hình nhỏ, sau đó mở
rộng cho máy tính.
Đơn giản và trực quan: Bố cục dễ nhìn, các nút chức năng quan trọng như giỏ
hàng, tìm kiếm luôn nổi bật.
Thẩm mỹ: Sử dụng màu sắc nhẹ nhàng, font chữ rõ ràng, hình ảnh sản phẩm chiếm
vị trí trung tâm.
3.2.3. Xây dựng cấu trúc thư mục dự án
Để thuận tiện trong quản lý và phát triển, dự án được tổ chức theo cấu trúc sau:
15

3.2.4. Phân tích và thiết kế giao diện
Wireframe sơ đồ bố cục các trang:
Trang chủ:
16

Danh mục sản phẩm:
Chi tiết sản phẩm:
3.2.5. Phát triển từng chức năng
Sau khi hoàn thiện thiết kế và cấu trúc, tiến hành lập trình giao diện theo từng chức
năng:
- Header và Footer: Cố định ở mọi trang, chứa menu điều hướng, logo, giỏ hàng,
tài khoản.
- Trang chủ (Home Page): Hiển thị banner, sản phẩm nổi bật, bộ sưu tập mới.
- Trang danh mục sản phẩm: Danh sách sản phẩm (size, màu, giá).
- Trang chi tiết sản phẩm: Hình ảnh sản phẩm, mô tả, tùy chọn size/màu, nút thêm
giỏ hàng.
17

- Giỏ hàng (Cart): Danh sách sản phẩm đã chọn, cập nhật số lượng, hiển thị tổng
tiền.
- Thanh toán (Checkout): Form nhập thông tin giao hàng, lựa chọn phương thức
thanh toán.
- Tài khoản người dùng: Đăng nhập, đăng ký, quản lý thông tin cá nhân.
3.3. Các chức năng chính đã thực hiện
Trong quá trình thực tập, em đã thiết kế và phát triển giao diện người dùng cho
ứng dụng web thương mại điện tử quần áo nữ với các chức năng chính sau:
Header và Footer:
Header: Gồm logo thương hiệu, thanh menu điều hướng (Áo, Quần, Đầm, Áo dài,
Sale…), thanh tìm kiếm sản phẩm, biểu tượng giỏ hàng và tài khoản người dùng.
Footer: Hiển thị thông tin liên hệ, chính sách mua hàng, hỗ trợ khách hàng, liên
kết mạng xã hội.
Đặc điểm: Header và Footer được cố định trên mọi trang, giúp người dùng dễ dàng
thao tác.
Trang chủ (Home page):
Hiển thị banner giới thiệu thương hiệu cùng slogan.
Giao diện thiết kế trực quan, ưu tiên hình ảnh sản phẩm lớn, dễ thu hút người dùng.
18

Trang Danh mục sản phẩm (Category page):
Hiển thị danh sách sản phẩm theo từng loại.
Trang Chi tiết sản phẩm (Product Detail page):
Hiển thị ảnh sản phẩm đa góc độ, tên, giá, mô tả chi tiết.
Cho phép chọn size, màu sắc, và số lượng trước khi thêm vào giỏ hàng.
Có gợi ý các sản phẩm tương tự để tăng trải nghiệm mua sắm.
19

Trang Giỏ hàng (Cart page):
Hiển thị danh sách các sản phẩm đã thêm.
Người dùng có thể thay đổi số lượng, xóa sản phẩm, và xem tổng tiền.
Có nút “Thanh toán” dẫn đến trang Checkout, và nút “quay lại” về trang Productdetail.
20

Trang Thanh toán (Checkout Page):
Form nhập thông tin giao hàng (họ tên, địa chỉ, số điện thoại).
Lựa chọn phương thức thanh toán (COD, thẻ ngân hàng, ví điện tử).
Hiển thị chi tiết đơn hàng để người dùng xác nhận trước khi hoàn tất.
3.4. Đánh giá kết quả đạt được
Sau thời gian thực tập và triển khai đề tài “Thiết kế và phát triển giao diện người dùng
cho ứng dụng web thương mại điện tử quần áo nữ sử dụng ReactJS”, em đã đạt được
một số kết quả cụ thể như sau:
21

Hoàn thiện giao diện cơ bản của ứng dụng thương mại điện tử: Các trang chính bao
gồm Trang chủ, Trang danh mục sản phẩm, Trang chi tiết sản phẩm, Giỏ hàng, Thanh
toán.
Ứng dụng thành công ReactJS trong phát triển giao diện: ReactJS giúp tổ chức mã
nguồn theo hướng component-based, dễ dàng tái sử dụng và mở rộng.
Đảm bảo trải nghiệm người dùng (UX): Bố cục giao diện được thiết kế đơn giản, trực
quan, dễ thao tác.
Rèn luyện và nâng cao kỹ năng chuyên môn:
Thành thạo hơn trong việc sử dụng Visual Studio Code, Node.js, npm, Vite để quản lý
và chạy dự án.
Biết cách triển khai và tối ưu UI/UX cho một ứng dụng web thực tế.
Phát triển kỹ năng tự nghiên cứu và giải quyết vấn đề khi gặp lỗi trong quá trình lập
trình.
Kết quả sản phẩm:
Ứng dụng đã đáp ứng các yêu cầu cơ bản đặt ra ban đầu: có tính thẩm mỹ, giao diện
hiện đại, hoạt động tốt trên nhiều thiết bị, hỗ trợ đầy đủ quy trình mua sắm trực tuyến từ
việc chọn sản phẩm đến thanh toán.
22

CHƯƠNG 4. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
4.1. Kết quả đạt được
Qua quá trình thực tập và triển khai đề tài “Thiết kế và phát triển giao diện người
dùng cho ứng dụng web thương mại điện tử quần áo nữ sử dụng ReactJS”, em đã đạt
được một số kết quả cụ thể như sau:
Hoàn thiện giao diện cơ bản của ứng dụng web thương mại điện tử với các trang
chính: Trang chủ, Trang danh mục sản phẩm, Trang chi tiết sản phẩm, Giỏ hàng, Thanh
toán và Tài khoản người dùng.
Thiết kế giao diện đáp ứng các yêu cầu UI/UX, giúp người dùng dễ thao tác, thuận
tiện trong quy trình mua sắm trực tuyến.
Thành thạo hơn trong việc sử dụng các công cụ phát triển như Visual Studio Code,
Node.js, npm, Vite, đồng thời nâng cao kỹ năng lập trình web và tối ưu trải nghiệm
người dùng.
Hoàn thiện một sản phẩm có tính ứng dụng thực tế, phù hợp với xu hướng thương
mại điện tử hiện nay.
4.2. Hạn chế và khó khăn
Bên cạnh những kết quả đạt được, đề tài vẫn còn một số hạn chế và khó khăn như
sau:
Ứng dụng mới dừng lại ở mức giao diện người dùng (frontend), chưa tích hợp hệ
thống backend và cơ sở dữ liệu để xử lý giỏ hàng, thanh toán và quản lý người dùng một
cách hoàn chỉnh.
Một số tính năng nâng cao (ví dụ: gợi ý sản phẩm thông minh, đánh giá của khách
hàng, quản lý đơn hàng) chưa được triển khai.
Do hạn chế về thời gian và kinh nghiệm, giao diện vẫn còn một số điểm cần cải
thiện về hiệu suất tải trang, tối ưu hình ảnh và khả năng truy cập cho mọi đối tượng
người dùng.
Khó khăn trong quá trình thực hiện chủ yếu đến từ việc tự nghiên cứu tài liệu tiếng
Anh và xử lý các lỗi phát sinh trong khi lập trình.
4.3. Hướng phát triển trong tương lai
Trong thời gian tới, để ứng dụng hoàn thiện và mang tính thực tiễn cao hơn, có thể
triển khai thêm các hướng phát triển sau:
23

Tích hợp backend và cơ sở dữ liệu: Kết nối với hệ thống server để quản lý sản
phẩm, người dùng, đơn hàng, giỏ hàng và thanh toán.
Bổ sung tính năng nâng cao:
Hệ thống gợi ý sản phẩm dựa trên hành vi người dùng.
Chức năng đánh giá, bình luận sản phẩm.
Tích hợp nhiều phương thức thanh toán phổ biến.
Tối ưu hiệu suất: Nén hình ảnh, sử dụng kỹ thuật lazy-loading và tối ưu mã nguồn
để cải thiện tốc độ tải trang.
Cải thiện UI/UX: Nghiên cứu xu hướng thiết kế mới, bổ sung hiệu ứng trực quan
và tối ưu trải nghiệm mua sắm trên thiết bị di động.
Triển khai thực tế: Đưa ứng dụng lên môi trường hosting hoặc dịch vụ cloud (như
Vercel, Netlify) để có thể sử dụng thử nghiệm và thu thập phản hồi từ người dùng.
24

TÀI LIỆU THAM KHẢO
[1] https://viblo.asia/p/reactjs-ma-nhieu-nguoi-dang-nhac-den-thich-hop-cho-nhung-
ung-dung-web-nao-d6BAMY03Rnjz
[2] https://www.freecodecamp.org/news/is-react-a-library-or-a-framework/
[3] https://bkacad.edu.vn/reactjs-va-react-native:-nhung-diem-khac-nhau-co-ban-
n.html
[4] https://vietnix.vn/react-js-la-gi/
[5] https://www.greenacademy.edu.vn/
·
25