str = 'tieN Cut'
print(str)

def hoa_thuong():
    # thường
    print(str.lower())
    # hoa
    print(str.upper())

def replace1():
    # replace(): thay thế 1 chuỗi con = chuỗi con khác
    print(str.replace("Cut","Ben"))

def split_():
    pass
    # tách chuỗi thành 1 ds
    str_split = "apple banana cherry"
    print(str_split.split())

def strip_():
    # loại bỏ khoảng trắng đầu - cuối chuỗi
    str_strip = " tien cut "
    print(str_strip)
    print(str_strip.strip())

def find_():
    # tìm kiếm chuỗi con trong chuỗi mẹ
    str_find = "tien cut"
    print(str_find.find("cut")) 

find_()