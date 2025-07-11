Câu 1:

- Ngôn ngữ biên dịch: là ngôn ngữ lập trình mà mã nguồn được dịch toàn bộ thành mã máy trước khi thực thi, thông qua một chương trình gọi là trình biên dịch (compiler). Tốc độ chạy nhanh hơn, nhưng khó phát hiện lỗi sớm.
  VD: Ngôn ngữ C++ (clang), C (gcc), Pascal (g++),...

- Ngôn ngữ thông dịch: là ngôn ngữ lập trình mà mã nguồn được thực thi trực tiếp bởi trình thông dịch (interpreter) không cần biên dịch trước thành mã máy.Tốc độ chạy chậm hơn tuy nhiên có thể báo lỗi ngay để fix.
  VD: Ngôn ngữ Python (.py), JavaScript (.js), PHP,...

=> Python là ngôn ngữ thông dịch vì mã Python được thực thi trực tiếp thông qua trình thông dịch, không cần thông dịch trước thành file máy.

""
Câu 2:

- Các kiểu dữ liệu trong Python:

  - int (số nguyên): -8; -5; 17; 4; ...
  - float (số thực): 0.5; 23.4; ...
  - complex (số phức): 4 + 17i
  - str (chuỗi ký tự): "hello"; '8506'; ...
  - bool (kiểu logic đúng/sai): true/false
  - list (danh sách): [1, 3, 5]
  - tuple (bộ dữ liệu không thay đổi): (2, 4, 6)
  - dict (từ điển): {"class": "HTTT01", "Truong":"CNTT va TT"}
  - set (tập hợp không chứa các phần tử trùng): {5, 7, 8}
  -

- Các kiểu toán tử trong Python:

  - Toán tử số học:

    - Cộng (+): 3 + 4 = 7
    - Trừ (-): 9 - 3 = 6
    - Nhân (_): 8 _ 9 = 72
    - Chia (/):(kq = (float)...): 5 / 2 = 2.5
    - Chia lấy phần nguyên (//): 5 // 2 = 2
    - Chia lấy phần dư (%): 5 % 2 = 1
    - Luỹ thừa (**): 8 ** 8 = 64

  - Toán tử so sánh:

    - so sánh bằng (==): a == b
    - Khác nhau (!=): a != b
    - Lớn hơn (>): a > b
    - Nhỏ hơn (<): a < b
    - Lớn hơn hoặc bằng (>=): a >= b
    - Nhỏ hơn hoặc bằng (<=): a <= b

  - Toán tử logic:

    - Và (and): a > 5 and b < 8
    - Hoặc (or): a < 17 or b > 4
    - Phủ định (not): not(a<9)

  - Toán tử gán:

    - (=): gán giá trị a = 13
    - (+=): cộng rồi gán a += 8
    - (-=): trừ rồi gán a -= 92
    - (/=): chia lấy phần thực rồi gán a /= 43
    - (//=): chia lấy phần nguyên rồi gán a //= 98
    - (%=): chia lấy phần dư rồi gán a %= 3
    - (_=): nhân rồi gán a _= 4
    - (**=): luỹ thừa rồi gán a **= 9

  - Toán tử bitwise:

    - & (and): a & b
    - | (or): a | b
    - ^ (xor): a ^ b
    - ~ (not): a ~ b
    - << (dịch sang trái): << a
    - > > (dịch sang phải): >> b

  - Toán tử kiểm tra thành viên:

    - in: trả về TRUE nếu giá trị có mặt trong chuỗi, list, hoặc set. 'a' in 'abc'
    - not in: trả về FALSE nếu giá trị không có mặt trong chuỗi, list, set hay tuple. 'x' not in 'abc'

  - Toán tử nhận dạng:
    - is: trả về TRUE nếu cả 2 biết đều tham chiếu đến cùng 1 đối tượng.
    - not is: trả về FALSE nếu 2 biến không tham chiếu đến cùng 1 dối tượng.

- Mệnh đề điều kiện và các loại vòng lặp(If else):

  - Mệnh đề điều kiện (If else)

    - if: thực hiện một câu/khối lệnh nếu điều kiện đúng.
    - elif: kiểm tra thêm điều kiện khác nếu if trước đó sai.
    - else: thực hiện một câu/khối lệnh nếu không có điều kiện if hoặc elif nào đúng.
      VD: x = 3
      if (x < 5);
      print ("x nhỏ hơn 5");
      elif (x == 3);
      prit ("x bằng 3");
      else;
      print ("x lớn hơn 5")

  - Vòng lặp for: lặp lại một đoạn mã nhiều lần, đặc biệt khi muốn duyệt qua các phần tử trong một dãy.

    VD:
    fruits = ["táo", "nho", "mận"]
    for fruit in fruits:
    print(fruit)

  - Vòng lặp while: lặp lại một đoạn mã khi điều kiện còn đúng. Nếu điều kiện sai, thoát khỏi vòng lặp.

    VD:
    password = ""
    while password != "1234":
    password = input("Nhập mật khẩu: ")
    print("Đăng nhập thành công!")

- Các câu lệnh điều khiển vòng lặp:

  - break; thoát khỏi vòng lặp ngay lập tức.
  - continue; Bỏ qua phần còn lại của vòng lặp hiện tại và chuyển sang phần tiếp theo.
  - pass; (giữ chỗ) tức là khôg làm gì cả nhưng vẫn đảm bảo cú pháp không bị lỗi.

- Kiểu dữ liệu TRUE, FALSE:

  - Có đúng 2 giá trị duy nhất là True/False.
  - Dùng nhiều trong so sánh, điều kiện, biểu thức logic
