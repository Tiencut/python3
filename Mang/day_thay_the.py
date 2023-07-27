n = int(input())
a = list(map(int,input().split()))


def tong_no_cong_nhan(n,a):
    tong_no = 0
    for i in range(n):
        if a[i] < 0:
            a[i] = 1
        elif a[i] > 0:
            a[i] = 2
    
    return a

tong_no_cong_nhan(n,a)

for i in range(n):
    print(a[i], end = " ")