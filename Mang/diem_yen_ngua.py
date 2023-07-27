# m: hàng, n: cột
m, n = map(int, input().split())

A = []
for i in range(m):
    hang = list(map(int, input().split()))
    A.append(hang)

# A[i][j] là điểm yên ngựa if (min hàng i, max cột j)
yeu_ngua = []
for i in range(m):
    for j in range(n):
        is_yen_ngua = True
        # Kiểm tra hàng
        for k in range(n):
            if A[i][k] < A[i][j]:
                is_yen_ngua = False
                break
        # Kiểm tra cột
        for k in range(m):
            if A[k][j] > A[i][j]:
                is_yen_ngua = False
                break
        if is_yen_ngua:
            yeu_ngua.append((i, j))

if not yeu_ngua:
    print("Khong co phan tu yen ngua")
else:
    print("Cac phan tu yen ngua la:")
    output_str = ''
    for h, c in yeu_ngua:
        output_str += '({},{}); '.format(h+1, c+1)

    print(output_str[:-2]+";")
