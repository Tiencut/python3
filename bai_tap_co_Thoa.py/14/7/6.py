import random

m,n = map(int,input().split())
# tạo mtr, số nguyên random, m dòng n cột
ma_tran = [ [random.randint(0,9) for col in range(n)] for row in range(m)]

def tong_cac_ptu_tren_cac_duong_bien_mtr(m,n,ma_tran):
    tong1 = 0
    # hàng trên
    for i in range(n):
        tong1 += ma_tran[0][i]
    # hàng dưới
    for i in range(n):
        tong1 += ma_tran[m-1][i]
    # cột trái
    for i in range(1,m-1):
        tong1 += ma_tran[i][0]
    # cột phải
    for i in range(1,m-1):
        tong1 += ma_tran[i][n-1]
    
    return tong1

def vi_tri_phan_tu_lon_nhat_dau_tien_mtr(m,n,ma_tran):
    vi_tri_ptu_max_dau_tien = "ma_tran[0][0]"
    max_mtr = 0
    for i in range(m):
        for j in range(n):
            if ma_tran[i][j] > max_mtr:
                max_mtr = ma_tran[i][j]
                vi_tri_ptu_max_dau_tien = (f"ma_tran[{i}][{j}]")
    print("vị trí phần tử max first",vi_tri_ptu_max_dau_tien)
    print()

def tong_ptu_nam_tren_dong_i(m,n,ma_tran):
    vi_tri = int(input("dòng muốn tính tổng? >=0 <m: "))
    tong2 = 0
    for i in range(n):
        tong2 += ma_tran[vi_tri][i]
    print(f"tổng ptu tại dòng {vi_tri} là: {tong2}")
    print()

def dong_co_tong_lon_nhat(m,n,ma_tran):
    tong2 = []
    row_max = 0
    row_co_sum_max = 0
    # tính tổng từng dòng
    for i in range(m):
        row_max = 0
        for j in range(n):
            row_max += ma_tran[i][j]
        tong2.append(row_max)
    print(tong2)
    # từ row_max, tìm vị trí có sum max
    max_list = max(tong2)
    print(max_list)
    for i in range(len(tong2)):
        if tong2[i] == max_list:
            row_co_sum_max = i
            break
    print(f"dòng {row_co_sum_max} có tổng ptu max là: {max_list}")

def sx_mtr_tang_dan(m,n,ma_tran):
    # chuyển về mtr 1 chiều
    ma_tran_sau_khi_chuyen_ve_mot_chieu = [ element for row in ma_tran for element  in row]
    # sort
    ma_tran_sort =  sorted(ma_tran_sau_khi_chuyen_ve_mot_chieu)
    # chuyển về mtr 2 chiều
    ma_tran_sau_khi_chuyen_ve_hai_chieu = [ ma_tran_sort[i:i+n] for i in range(0,len(ma_tran_sort),n) ]
    
    print("ma trận sau khi sắp xếp tăng dần")
    for row in ma_tran_sau_khi_chuyen_ve_hai_chieu:
        print(' '.join([str(elem) for elem in row]))

# in mtr
for row in ma_tran:
    print(' '.join([str(elem) for elem in row]))
# Gọi các hàm và in kết quả
tong = tong_cac_ptu_tren_cac_duong_bien_mtr(m, n, ma_tran)
print("Tổng các phần tử trên các đường biên của ma trận:", tong)

vi_tri_phan_tu_lon_nhat_dau_tien_mtr(m, n, ma_tran)

tong_ptu_nam_tren_dong_i(m, n, ma_tran)

dong_co_tong_lon_nhat(m, n, ma_tran)

sx_mtr_tang_dan(m, n, ma_tran)