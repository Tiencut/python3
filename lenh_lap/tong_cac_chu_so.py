n = str(abs(int(input())))

def tinh_co_dau_am(n):
    tong_cac_chu_so = 0
    check_co_dau_am_khong = False
    for i in n:
        # check co "-" ?
        if i == "-":
            check_co_dau_am_khong = True
            continue
        
        if i.isdigit():
            i = int(i)
            if check_co_dau_am_khong:
                i *=-1
                check_co_dau_am_khong = False
            tong_cac_chu_so += i

    print(tong_cac_chu_so)

def tinhg_k_dau_am(n):
    tong_cac_chu_so = 0
    for i in n:
        tong_cac_chu_so += int(i)
    
    print(tong_cac_chu_so)

def tinhg_k_dau_am_list_comprehension(n):
    tong_cac_chu_so = sum([int(i) for i in n])
    print(tong_cac_chu_so)

tinhg_k_dau_am_list_comprehension(n)