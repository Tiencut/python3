# use lưu trữ gtr dât trong cặp key:value
# sx theo thứ tự *, có thể thay đổi, ko trùng
# có thể thay đổi (add,delete) sau khi tạo
sinhVien = {
    "hoVaTen" : "Nguyen Van A",
    "maLop" : "DH01",
    "diemTrungBinh" : 8.5
}

# print(sinhVien)

# print(sinhVien["hoVaTen"])

# x = sinhVien.get("maLop")
# print(x)

# thay đổi gtr
# sinhVien["maLop"] = "DH02"
# print(sinhVien)
# sinhVien.update({"maLop":"DH03", "diemTrungBinh":8.5})
# print(sinhVien)

# # add
# sinhVien["namHoc"] = 2023
# print(sinhVien)
# sinhVien.update({"noiSinh":"Hue"})
# print(sinhVien)

# # delete
# ## phương thức pop() --> delete mục có tên khoá đc chỉ định
sinhVien.pop("maLop")
print(sinhVien)
# ## phương thức popitem() --> xoá cái cuối cùng
# sinhVien.popitem()
# print(sinhVien)
# ## từ khoá del
# del sinhVien["hoVaTen"]
# print(sinhVien)

# del sinhVien
# print(sinhVien)

# phương thức clear() --> xoá all gtri

# duyệt

## duyệt tên khoá
# for x in sinhVien:
#     print(x)
# '''or'''
# for x in sinhVien.keys():
#     print(x)

# ## duyệt gtri
# for x in sinhVien.values():
#     print(x)

## duyệt khoá-gtr
# for x, y in sinhVien.items():
#     print(x, y)
