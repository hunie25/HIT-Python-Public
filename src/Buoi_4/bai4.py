n = int(input("Nhập n: "))

a = []
for i in range(n):
    x = input(f"Nhập phần tử thứ {i+1}: ")
    a.append(x)

b = tuple(a)

print("Tuple b là:", b)

count_digit_strings = sum(1 for item in b if item.isdigit())
print("Số phần tử có dạng số trong tuple b là:", count_digit_strings)
