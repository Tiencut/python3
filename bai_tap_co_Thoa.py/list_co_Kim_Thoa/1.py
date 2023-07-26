n = int(input())
ds_so_nguyen = list(map(int,input().split()))

# loại phần tử tùng
ds_so_nguyen_khong_trung = list(set(ds_so_nguyen))
print(f"số phần tửu pb trong ds là: {len(ds_so_nguyen_khong_trung)}")

# đếm sl ptu > phần từ đứng trước-sau
sl_ptu_lon_hon_ptu_truoc_sau = 0
for i in range(n):
    if ds_so_nguyen[i] > ds_so_nguyen[i-1] and ds_so_nguyen[i] < ds_so_nguyen[i+1]:
        sl_ptu_lon_hon_ptu_truoc_sau += 1
print(sl_ptu_lon_hon_ptu_truoc_sau)