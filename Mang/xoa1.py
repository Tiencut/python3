m, n = map(int, input().split())
# nhập ma trận
A=[]
for i in range(m):
    row = list(map(int,input().split()))
    A.append(row)
# tìm điểm yên ngựa (min_in_row, max_in_column)
diem_yen_ngua = []
for i in range(m):
    for j in range(n):
        min_in_row = max_in_column = True
        # check min_in_row
        for k in range(n):
            if A[i][k] < A[i][j]:
                min_in_row = False
        # check column
        for k in range(n):
            if A[k][j] > A[i][j]:
                max_in_column = False
        if min_in_row and max_in_column:
            diem_yen_ngua.append((i+1,j+1))

print("Cac diem yen ngua la:")
output_str = ""
for row, col in diem_yen_ngua:
    output_str += '({},{}); '.format(row,col)
print(output_str[:-2]+";")