n = int(input("n? "))

import numpy as np;import random

# tạo 2 ma trận vuông size n random, chứa trong kiểu list
a1 = [ [random.randint(0,10) for j in range(n)] for i in range(n)]
a2 = [ [random.randint(0,10) for j in range(n)] for i in range(n)]

print(a1);print(a2)

def tich_hai_ma_tran(a1,a2,n):
    a3 = [ [ 0 for j in range(n)] for i in range(n)]
    
    for row in range(n):
        for col in range(n):
            for tmp in range(n):
                a3[row][col] += a1[row][tmp] * a2[tmp][col]
    
    return a3


def tich_hai_ma_tran_cach_cua_co(a,b,n):
    c = []
    for row in range(n):
        r = []
        for col in range(n):
            s = 0
            for tmp in range(n):
                s += a[row][tmp]*b[tmp][col]
            r.append(s)
        c.append(r)
    return c

a3 = tich_hai_ma_tran(a1,a2,n)
print("tich hai ma tran")
print(a3)

# # chuyển 2 ma trận về kiểu array của numpy
# print();print(f"2 ma trận, dùng numpy")
print(f"tich 2 ma trận, dùng numpy")
b1 = np.array(a1)
b2 = np.array(a2)
print(np.dot(b1, b2))