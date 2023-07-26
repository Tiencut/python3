# Tạo một từ điển lưu số ngày ứng với 12 tháng của năm 2020 sau đó cho phép:
tu_dien_thang = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

#  In  các tháng có 31 ngày 
def in_thang_31_ngay(tu_dien_thang):
    print("những tháng có 31 ngày là: ",end=" ")
    for thang,songay in tu_dien_thang.items():
        if songay == 31:
            print(f"{thang}",end=" ")
    print()

# Nhập vào một tháng và in ra số ngày  của tháng đó
def nhap_1_thang_in_ra_so_ngay_thang_do(tu_dien_thang):
    thang_nhap = int(input())
    for thang,songay in tu_dien_thang.items():
        if thang_nhap == thang:
            print(f"số ngày của tháng {thang} là {songay}")

in_thang_31_ngay(tu_dien_thang)

nhap_1_thang_in_ra_so_ngay_thang_do(tu_dien_thang)