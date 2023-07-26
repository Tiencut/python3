n = int(input())

for i in range(n):
    print(1, end = " ")
    kq = 1
    for j in range(i):
        kq = kq*(i-j)//(j+1)
        print(kq, end = " ")
    print()
