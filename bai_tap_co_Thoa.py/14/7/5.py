import math

n_list = list(map(int,input().split()))

max_in_list = max(n_list)
print(f"ptu max: {max_in_list}")

min_in_list = min(n_list)
print(f"ptu min: {min_in_list}")

def nhung_ptu_la_so_nguyen_to(n_list):
    list_snt = []
    
    def check_snt(so):
        if so < 2:
            return False
        for i in range(2,int(math.sqrt(so))+1):
            if so % i == 0:
                return False
        return True
    
    for i in n_list:
        if check_snt(i):
            list_snt.append(i)
    
    print(f"nhung ptu la số nguyên tố là: {list_snt}")

nhung_ptu_la_so_nguyen_to(n_list)

def tong_binh_phuong_cac_ptu_am(n_list):
    tong_am = sum(i**2 for i in n_list if i < 0)
    return tong_am

print("tổng bình phương các số âm: ",tong_binh_phuong_cac_ptu_am(n_list))

