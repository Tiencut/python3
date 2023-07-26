import math
# diện tích hình tròn
def dien_tich_hinh_tron():
    r = float(input())
    S = math.pi*r*r
    print(S)

# # giải ptr bậc nhất a.x+b = 0
def giai_ptr_bac_1():
    a,b = map(int,input().split())
    if a == 0:
        if b == 0:
            print("vô số nghiệm")
        else:
            print("vô nghiệm")
    else:
        x = -b/a
        print("nghiệm: ",x)

# giải ptr bậc 2 a.x^2 + b.x + c = 0
def giai_ptr_bac_2():
    a,b,c = map(int,input().split())
    delta = b**2 - 4*a*c
    if delta == 0:
        print( (-b + math.sqrt(delta)) / (2*a)  )
        print( (-b - math.sqrt(delta)) / (2*a)  )
    elif delta > 0:
        print((-b/(2*a)))
    else:
        print("vô nghiệm")

# tính tiền điện theo KWh tiêu thụ, use bảng giá điện Huế
# Bậc 1: kWh: 0 - 50,   giá bán điện (đồng/kWh): 1.678 1.6
# Bậc 2: kWh: 51 - 100, giá bán điện (đồng/kWh): 1.734 1.7
# Bậc 3: kWh: 101 - 200,giá bán điện (đồng/kWh): 2.014 2
# Bậc 4: kWh: 201 - 300,giá bán điện (đồng/kWh): 2.536 1.6
# Bậc 5: kWh: 301 - 400,giá bán điện (đồng/kWh): 2.834 2.8
# Bậc 6: kWh: 201 - 300,giá bán điện (đồng/kWh): 2.927 2.9
def tinh_tien_dien():
    so_dien_da_use = float(input())
    tien_dien = 0

    if so_dien_da_use <= 50:
        tien_dien = so_dien_da_use*1.678
    elif so_dien_da_use <= 100 and so_dien_da_use > 50:
        tien_dien = 50*1.678 + (so_dien_da_use-50)*1.734
    elif so_dien_da_use <= 200 and so_dien_da_use > 100:
        tien_dien = 50*1.678 + 50*1.734 + (so_dien_da_use-100)*2.014
    elif so_dien_da_use <= 300 and so_dien_da_use > 200:
        tien_dien = 50*1.678 + 50*1.734 + 100*2.014 + (so_dien_da_use-200)*2.536
    elif so_dien_da_use <= 400 and so_dien_da_use > 300:
        tien_dien = 50*1.678 + 50*1.734 + 100*2.014 + 100*2.536 + (so_dien_da_use-300)*2.834
    elif so_dien_da_use  > 400:
        tien_dien = 50*1.678 + 50*1.734 + 100*2.014 + 100*2.536 + 100*2.834 + (so_dien_da_use-400)*2.927

    print(tien_dien)

def tinh_tien_dien_cach2():
    so_dien_da_use = float(input())
    tien_dien = 0
    gia_dien_theo_bac = [1.678,1.734,2.014,2.536,2.834,2.927]
    dien_theo_bac = [50,50,100,100,100,100]
    bac_tien_dien = 0

    for i in range(6):
        if so_dien_da_use <= 0:
            break
            
        tien_dien += min(so_dien_da_use,dien_theo_bac[i]) * gia_dien_theo_bac[i]
        so_dien_da_use -= min(so_dien_da_use,dien_theo_bac[i])

    print(tien_dien)



# tính số tiền thu được sau n tháng
# ban đầu: a
# lãi: k
# lãi cộng dồn vào tiền gửi tiết kiệm
def lai_ngan_hang():
    a,k,n = map(float,input().split())
    money_thu_duoc_sau_n_thang = a
    for i in range(int(n)):
        lai_moi_thang = money_thu_duoc_sau_n_thang*(k/100)
        money_thu_duoc_sau_n_thang += lai_moi_thang
    print(money_thu_duoc_sau_n_thang)