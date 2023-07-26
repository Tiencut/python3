n = int(input())
a = list(map(int,input().split()))


def tong_no_cong_nhan(n,a):
    tong_no = 0
    for i in range(n):
        if a[i] < 0:
            tong_no += a[i]

    
    return tong_no

print(tong_no_cong_nhan(n,a))