m,n,p = map(int, input().split())

A = []
B = []

# m dòng, chứa n số nguyên ( gtri từng hàng của mtr A) (mtr A: 1xN)
for i in range(m):
    row_A = list(map(int, input().split()))
    A.append(row_A)

# n dòng, chứa p số nguyên ( gtri từng hàng của mtr B:NxP)
for i in range(n):
    row_B = list(map(int, input().split()))
    B.append(row_B)

# tạo mtr 1xP lưu kết quả (m hàng, P cột)
ket_qua = [ [0 for j in range(p)] for i in range(m)]

# tính
''' 
lấy từng hàng của mtr A
nhân từng cột của mtr B
'''
for i in range(m):
    for j in range(p):
        for k in range(n):
            ket_qua[i][j] += (A[i][k] * B[k][j])


# in kết quả
for row in ket_qua:
    print(' '.join([str(elem) for elem in row] ))
