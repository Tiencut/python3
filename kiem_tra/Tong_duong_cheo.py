n = int(input())

list_n = []
for i in range(n):
    tmp = list(map(int,input().split()))
    list_n.append(tmp)

def tong_cheo_chinh_va_phu(n,list_n):
    tong_duong_cheo_chinh = 0
    tong_duong_cheo_phu = 0    
    j = 0
    k = n-1

    for i in range(n):
        tong_duong_cheo_chinh += list_n[i][j]
        tong_duong_cheo_phu += list_n[i][k]                
        j += 1
        k -= 1

    cai_can_tru = list_n[n//2][n//2]
    
    if n % 2 == 0:   
        print(tong_duong_cheo_chinh + tong_duong_cheo_phu)
    else:
        print(tong_duong_cheo_chinh + tong_duong_cheo_phu - cai_can_tru)

tong_cheo_chinh_va_phu(n,list_n)