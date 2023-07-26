# QLSV
print("QUẢN LÝ SINH VIÊN = DICTIONARY")
print("1.ADD SV(MASV, TEN)")
print("2.output ds n sv")
print("3.find sv")
print("4.delete sv")
print("5.thoát")

ds_sv = {}

while(True):
    lua_chon = int(input("lựa chọn? "))

    if lua_chon == 1:
        masv, tensv = map(str,input("masv? tensv?").split())
        ds_sv[masv] = tensv
    elif lua_chon == 2:
        if len(ds_sv) == 0:
            print("ds rỗng")
        else:
            for masv,tensv in ds_sv.items():
                print(f"masv: {masv}, tên: {tensv}")
    elif lua_chon == 3:
        if len(ds_sv) == 0:
            print("ds chưa có sv")
            continue
        masv_muon_find = input("masv cần tìm?")
        if masv_muon_find == masv:
            print(f"masv: {masv}, ten: {tensv}")
        else:
            print(f"k find sv với masv: {masv_muon_find}")
    elif lua_chon == 4:
        masv_muon_del = input("masv cần del?")
        if masv_muon_find in ds_sv:
            del ds_sv[masv]
            print("delete thành công")
        else:
            print(f"k find masv: {masv_muon_del} để xoá")
    elif lua_chon == 5:
        break
    else:
        print("lựa chọn không hợp lệ")

print("end program")