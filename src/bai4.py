
n = int(input("Nhập số xu: "))
price = 28
so_chai = n // price
so_vo = so_chai

while so_vo >= 3:
    doi = so_vo // 3
    so_chai += doi
    so_vo = so_vo % 3 + doi
print("Số chai bia có thể mua được là:", so_chai)
