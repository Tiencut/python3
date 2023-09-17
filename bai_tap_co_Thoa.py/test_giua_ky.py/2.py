s = input("chuỗi? ")

def cau_1(s):
    def check_str_doi_xung(s):
        return s == s[::-1]

    if check_str_doi_xung(s):
        print("xâu đối xứng")
    else:
        print("không phải là xâu đối xứng")

def cau_2(s):
    ki_tu_can_xoa = input("kí tự cần xoá? ")
    tmp = ""
    for i in s:
        if i == ki_tu_can_xoa:
            continue
        tmp += i
    print(tmp)

cau_2(s)