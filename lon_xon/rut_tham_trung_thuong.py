import random

# Khai báo set
thung_phieu = set()

while True:
    print("---Menu---")
    print("1. Thêm")
    print("2. Xóa")
    print("3. Ngẫu nhiên")
    print("4. Kết thúc")
    print(thung_phieu)

    lua_chon = int(input("Lựa chọn? "))

    if lua_chon == 1:
        so_dien_thoai = input("Nhập số điện thoại: ")
        thung_phieu.add(so_dien_thoai)
    elif lua_chon == 2:
        so_dien_thoai = input("Số điện thoại cần xóa: ")
        thung_phieu.discard(so_dien_thoai)
    elif lua_chon == 3:
        if len(thung_phieu) > 0:
            i = random.randint(0, len(thung_phieu) - 1)
            random_phone = list(thung_phieu)[i]
            print(random_phone)
        else:
            print("Danh sách trống.")
    elif lua_chon == 4:
        break
