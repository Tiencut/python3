n = int(input("ds n sv? "))

SinhVien = []
# nhập n sv
for i in range(n):
    SinhVien.append({
        "masv"      : input("masv? "),
        "ho_ten"    : input("ho_ten? "),
        "khoa"      : input("khoa? "),
        "diem_tb"   : float(input("diem_tb? "))
    })

# in sv khoa Toán
sinh_vien_toan = [sinhvien for sinhvien in SinhVien if sinhvien["khoa"] == "Toán" ]
for i in sinh_vien_toan:
    print(i)
print()
# in sv diem_tb >= 8
sinh_vien_diem_tb = [ sv for sv in SinhVien if sv["diem_tb"] >= 8]
for i in sinh_vien_diem_tb:
    print(i)
print()
# sx sv tăng dần theo diem_tb
sinh_vien_diem_tb_tang_dan = sorted(SinhVien,key = lambda sv:sv["diem_tb"])
for i in sinh_vien_diem_tb_tang_dan:
    print(i)

sorted(SinhVien,key=lambda x:x["diem_tb"])