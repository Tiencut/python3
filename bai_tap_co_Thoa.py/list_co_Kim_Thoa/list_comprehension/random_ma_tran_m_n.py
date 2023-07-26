import random

m,n = map(int,input().split())

def crete_ma_tran_bang_list_comprehension(m,n):
    return [ [ random.randint(1,9) for column in range(n)] for row in range(m)]

def crete_ma_tran_bang_for(m,n):
    M1 = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp1 = random.randint(0,9)
            tmp.append(tmp1)
        M1.append(tmp)
    return M1

M1 = crete_ma_tran_bang_list_comprehension(m,n)
M2 = crete_ma_tran_bang_for(m,n)

print(M1)
print(M2)

M3 = [ [ M1[row][column] + M2[row][column] for column in range(n)] for row in range(m)]
print(M3)

