A = {'001', '002', '003', '004', '007'}
B = {'003', '006', '002', '007', '009', '034', '462'}

A_and_B = A.intersection(B)
A_union_B = A.union(B)
A_diff_B = A.difference(B)

print('Những sinh viên đăng ký học cả hai bàn là:', A_and_B)
print('Danh sách tổng hợp sinh viên đã đăng ký:', A_union_B)
print('Sinh viên đăng ký tại bàn 1 mà không đăng ký tại bàn 2:', A_diff_B)
