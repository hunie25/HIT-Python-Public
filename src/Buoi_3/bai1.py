n = int (input("nhap n: "))
DS = [int(input("nhap ptu thu {i+1}: ")) for i in range (n)]

x = int (input("nhap x: "))
print(f"so lan xuat hien cua {x} trong list la:  {DS.count(x)}")

if len (DS) >= 7:
    DS[1:7] = [8, 5, 4, 0, 1, 3]
    print("list sau khi thay the la: ", DS)
else:
    print("list qua ngan")

print("so lon nhat:", max(DS))
print("so nho nhat:", min(DS))

y = int(input("nhap Y: "))
DS.insert(0, y)
print("List sau khi chèn:", DS)

if DS == sorted(DS):
    print("tang")
elif DS == sorted(DS, reverse=True):
    print("giam")
else:
    print("no")

