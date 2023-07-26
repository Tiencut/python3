n = int(input())

# tổng các ước số = chính nó
def check_so_hoan_hao(n):
    tong_uoc_So = 1
    for i in range(2,n//2):
        if n % i == 0:
            tong_uoc_So += i
    return n == tong_uoc_So

if check_so_hoan_hao(n):
    print("Yes")
else:
    print("No")