n = int(input("Nhập n: "))
n_str = str(n)

dem = len(n_str)
tong = sum(int(ch) for ch in n_str)

print("Số chữ số:", dem)
print("Tổng chữ số:", tong)