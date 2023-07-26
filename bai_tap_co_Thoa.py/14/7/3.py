n = int(input())
n_list = list(map(int,input().split()))

n_list_set = list(set(n_list))
so_phan_tu_khac_biet_trong_list = len(n_list_set)
print(f"so phan tu khac nhau trong list: {so_phan_tu_khac_biet_trong_list}")

def dem_so_ptu_lon_hon_so_dung_truoc_va_sau_no(n_list):
    so_ptu_lon_hon_so_dung_truoc_va_sau_no = 0
    for i in range(1,len(n_list)-1):
        if n_list[i] > n_list[i+1] and n_list[i] > n_list[i-1]:
            so_ptu_lon_hon_so_dung_truoc_va_sau_no += 1
    return so_ptu_lon_hon_so_dung_truoc_va_sau_no

print(dem_so_ptu_lon_hon_so_dung_truoc_va_sau_no(n_list))