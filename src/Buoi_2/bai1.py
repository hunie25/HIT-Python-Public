thang = int (input("nhap thang: "))
nam = int (input("nhap nam: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print ("31")
elif thang in [4, 6, 9, 11]:
    print ("30")
else:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print ("29")
    else:
        print ("28")
