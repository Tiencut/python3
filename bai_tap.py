import math
def quan_ly_diem_hoc_phan():
    n = int(input())
    for i in range(n):
        diem_QTHT, diem_thi = map(float,input().split())
        diem_KTHP = diem_QTHT*0.4 + diem_thi*0.6

        def bang_quy_doi_diem(diem):
            if diem < 4.0:
                return 'F'
            elif diem < 5.5:
                return 'D'
            elif diem < 7:
                return 'C'
            elif diem < 8.5:
                return 'B'
            elif diem < 10.0:
                return 'A'
        
        diem_KTHP_lam_tron = round(diem_KTHP,1)
        print(f"{diem_KTHP_lam_tron} {bang_quy_doi_diem(diem_KTHP_lam_tron)}")



def tim_so_chu_dao_ngay_sinh(ngay_sinh):
    # chuẩn hoá về dạng dd/mm/yyyy
    ngay_sinh = ''.join(ngay_sinh.split())
    print(ngay_sinh,end=" ")

    # tổng số có trong ngày sinh đến khi nằm = [2,11]
    tong_so_trong_ngay_sinh = sum( int(i) for i in ngay_sinh if i.isdigit())

    def tong_cac_chu_so(so):
        tmp = 0
        while so>0:
            tmp += so%10
            so //= 10

        return tmp

    while tong_so_trong_ngay_sinh > 11:
        tong_so_trong_ngay_sinh = tong_cac_chu_so(tong_so_trong_ngay_sinh)
    
    print(tong_so_trong_ngay_sinh)

def check_snt(so):
    if so < 2: return False
    for i in range(2,int(math.sqrt(so))):
        if so % i == 0: return False
    return True

def snt_1():
    for i in range(2,101):
        if check_snt(i):
            print(i,end=" ")

def so_hoan_hao(so):
    tmp = 1
    for i in range(2,so):
        if so % i == 0:
            tmp += i
    return so == tmp

# if so_hoan_hao(6):
#     print('tien')
# else:
#     print('cut')

def rut_gon_phan_so(a,b):
    def ucln(a,b):        
        while b > 0:
            a,b = b, a % b
        return a
    ucmax = ucln(a,b)
    print(f"{a/ucmax}/{b/ucmax}")




def cau_6(A,B):
    # tạo và ghi dữ liệu file SONNGUEN.INP
    with open("SONNGUYEN.INP","w") as f:
        f.write('34\n610')

    # Đọc data đầu vào từ file SONNGUYEN.INP
    with open("SONNGUYEN.INP","r") as f:
        A,B = f.readlines()
        A = A.strip()
        B = B.strip()

    # Tạo list các chữ số của A,B
    digits_A = list(A)
    digits_B = list(B)

    # Tạo list các chữ số của Cmax (chèn đầu)
    digits_Cmax = digits_A + digits_B
    Cmax = int(''.join(digits_Cmax))

    A_str = ''.join(digits_A)
    for i in range(1,len(digits_B)):
        # Chèn chuỗi A vào vị trí thứ i của list B
        B_str = digits_B[:]
        B_str.insert(i, A_str)
        tmp = int(''.join(B_str))

        if tmp > Cmax:
            Cmax = tmp

    with open("SONNGUYEN","w") as f:
        f.write(str(Cmax))

cau_6(34,610)