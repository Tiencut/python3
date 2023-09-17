def chuan_hoa_chuoi(str):
    # input: tien//cut
    # output: tien/cut

    # cách 1
    return str.replace("//","/")

    # cách 2
    # list_chuoi = str.split('//')
    # new_str = '/'.join(list_chuoi)
    # return new_str

def check_chuoi_toan_so(str):
    if str.isdigit():
        return True
    else:
        return False

def chuyen_thuong_ve_hoa(str):
    # chuyển về chữ thường, kí tự đầu viết hoa
    # không chứa dấu space thừa
    # các dấu câu có 
    str = str.lower().strip().split()
    str = " ".join(str)

    return str.capitalize()

def tach_ten(str):
    str = list(str.split())
    print(str[len(str)-1])

def dem_so_lan_xuat_hien_ki_tu(ho_ten,tmp):
    return ho_ten.count(tmp)
    
print(dem_so_lan_xuat_hien_ki_tu("Dao Thi Hoa Hong Mai","ai"))