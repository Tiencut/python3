# # 
# L = [ [2]*5 for i in range(10) ]

# # 
# M = [ col for row in L for col in row ]
# print(L)
# print(len(M))

# random 2 mtr size mxn
m,n = map(int,input().split())
# 
A = []
print("nhap mtr A")
for i in range(m):
    tmp1 = list(map(int,input().split()))
    A.append(tmp1)
# 
B = []
print("nhap mtr B")
for i in range(m):
    tmp1 = list(map(int,input().split()))
    B.append(tmp1)
# 
C = []
for row in range(m):
    tmp = []
    for col in range(n):
        tmp.append(A[row][col]+B[row][col])
    C.append(tmp)

print(C)