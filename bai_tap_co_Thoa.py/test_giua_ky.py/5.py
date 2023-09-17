n  = int(input("ds n sv? "))

SinhVien = []

for i in range(n):
    SinhVien.append({
        "masv":input("masv? "),
        "hoTen":input("họ tên? "),
        "khoa":input("khoa?  "),
        "diem_tb":float(input("điểm trung bình? "))
    })

# a.Lọc, in sinh viên thuộc khoa toán
SinhVien_toan = [sinhvien for sinhvien in SinhVien if sinhvien["khoa"] == "Toán"]
for sinhVien_i in SinhVien_toan:
    print(sinhVien_i)

# b.Lọc, in sinh viên  điểm tb>=8 để cấp học bổng
sinhVien_dtb = [ sinhvien for sinhvien in SinhVien if sinhvien["diem_tb"] >= 8]
for sinhvien_i in sinhVien_dtb:
    print(sinhvien_i)

# c.sx, in  danh sách sv  tăng dần của điểm tb.
sinhVien_sort_diem_tb_tang = sorted(SinhVien,key=lambda sv:sv["diem_tb"])

for sinhvien_i in sinhVien_sort_diem_tb_tang:
    print(sinhvien_i)