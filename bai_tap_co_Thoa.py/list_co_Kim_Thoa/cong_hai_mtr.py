m,n = map(int,input().split())

# nhập ma trận A
A = []
print("nhập mtr A")
for i in range(m):
    row = list(map(int,input().split()))
    A.append(row)
# nhập ma trận B
B = []
print("nhập mtr B")
for i in range(m):
    row = list(map(int,input().split()))
    B.append(row)

C = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(A[i][j]+B[i][j])
    C.append(tmp)
print(C)
for row in C:
    print(' '.join( [str(elem) for elem in row] ))