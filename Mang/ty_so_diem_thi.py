n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def ty_so_diem_thi(n,a,b):
    diem_cua_a = 0
    diem_cua_b = 0

    for i in range(n):
        if a[i] > b[i]:
            diem_cua_a += 1
        elif a[i] < b[i]:
            diem_cua_b += 1
    
    print(diem_cua_a, " ", diem_cua_b)

ty_so_diem_thi(n,a,b)