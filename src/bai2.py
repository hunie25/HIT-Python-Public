luong = int (input ("nhap luong: "))
thue = 0
thu_nhap = 0
if luong < 7000000:
    thue = luong * 10 / 100
elif luong >= 7000000 and luong <= 15000000:
    thue = luong *20 / 100
else:
    thue = luong * 30 / 100
print(f"thue: {thue} + thu nhap:{luong - thue}")
