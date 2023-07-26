x = float(input())
n = 0
term = 1
S = term

while abs(term) >= 10**-9:
    n += 1
    term *= x / n
    S += term

print("{:.4f}".format(S))

'''
tính tổng S = 1 + x/1! + x**2/x! + ... + x**n/n!
abs(x**n/n!) < 10**-9

x: số thực nhập từ bàn phím
kết quả làm tròn 4 chữ số sau dấu chấm
'''