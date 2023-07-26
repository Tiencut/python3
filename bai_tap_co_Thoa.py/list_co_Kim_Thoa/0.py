# tạo list chứa 100 số nguyên random trong [1,9]:
import random
def bai_1():
    A = []
    for i in range(100):
        x = random.randint(1,9)
        A.append(x)

    # 1. in dãy
    print(A)

    # 2. trung bình cộng dãy số
    trung_binh_cong_day = sum(A) / len(A)
    print("Trung bình cộng dãy",trung_binh_cong_day)

    # 3. số lần xuất hiện ứng với các số 1,2,...9
    for i in range (1,10):
        so_lan_xuat_hien = A.count(i)
        print(f"so {i} xuat hien {so_lan_xuat_hien}")

# nhập ds, dùng for sx tăng dần (ko sort)
def bai_2():
    # nhập list
    A = list(map(int,input().split()))
    # sx tăng dần
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] < A[j]:
                A[i],A[j] = A[j],A[i]
    # in
    print(A)

# nhập ds n sinh viên( "masv" : diemktr(thang 10))
# in ds thang diem 4 (A,B,C,D,F)
# in ds theo diem kt giảm dần
def bai_3():  
    def input_n_sv():
        n = int(input("sl sv sẽ nhập? "))
        ds_sv = {}
        for i in range(n):
            masv = input("masv? ")
            diem = float(input("diem? "))
            ds_sv[masv] = diem
        return ds_sv
    
    def chuyen_doi_diem(diem):
            if diem >= 9:
                return "A"
            elif diem >= 8:
                return "B"
            elif diem >= 7:
                return "C"
            elif diem >= 5:
                return "D"
            else:
                return "F"
    
    def in_ds_sv_thang_diem_4(ds_sv):    
        for masv, diem in ds_sv.items():
            print(f"masv: {masv}, diem: {chuyen_doi_diem(diem)}")
    
    def in_sv_diem_giam_dan(ds_sv):
        sorted_ds = sorted(ds_sv.items(),key=lambda x: x[1],reverse=True)
        for masv, diem in sorted_ds:
            print(f"masv: {masv}, diem: {ds_sv[masv]}")
    # nhập ds sv
    ds_sv = input_n_sv()
    # in ds theo thang điểm 4
    in_ds_sv_thang_diem_4(ds_sv)
    # in ds điểm giảm dần
    in_sv_diem_giam_dan(ds_sv)

# bài 4: nhập 2 ma trận cùng size, + 2 ma trận lại
def bai_4():
    m,n = map(int,input("cột? hàng?").split())
    print("nhập mtr A")
    A = []
    for i in range(m):
        row = list(map(int,input().split()))
        A.append(row)
    print("nhập mtr B")
    B = []
    for i in range(m):
        row = list(map(int,input().split()))
        B.append(row)
    # tính tổng 2 ma trận
    C = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(A[i][j]+B[i][j])
        C.append(tmp)
    # in ma trận
    print("in ma trận")
    for row in C:
        print(' '.join([str(elem) for elem in row] ) )

bai_4()

