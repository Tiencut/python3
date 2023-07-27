m,n = map(int,input().split())

A = []
for i in range(m):
    hang = list(map(int,input().split()))
    A.append(hang)

# list comprehension kkk khá gọn
B = [[0 for j in range(m)] for i in range(n)]
# code dòng 8 có nghĩa giống dưới
# B = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(0)
#     B.append(row)

# 
for i in range(m):
    for j in range(n):
        B[j][i] = A[i][j]
# in ma trận  
for hang in B:
    print(' '.join(map(str,hang)),end = "\n")

# print()
# for j in range(n):
#     for i in range(m):
#         print(B[j][i],end=" ")
#     print()