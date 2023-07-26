# hỏi tên gì, nhập tên, in "Chào bạn"
def bai_1():
    x = "tien"
    print("tên gì?")
    s1 = input("nhập tên? ")
    print("Chào bạn",s1)
    if s1 == x:
        print("cùng tên với tôi")
    else:
        print("không cùng tên với tôi")

def bai_2():
    s2 = input()
    print(s2.replace("*","@"))

# nhập họ tên, in tên
def bai_3():
    full_name = input()
    # lưu từng tên vào list
    name_list = full_name.split()
    print(name_list)
    last_name = name_list[-1]
    print("Chao",last_name)

# số bước biến đổi đề được 1 xâu đối xứng
def bai_4():
    def check_doi_xung(s):
        return s == s[::-1]

    xau = input()
    so_buoc_bien_doi = 0

    if check_doi_xung(xau):
        return so_buoc_bien_doi
    # đếm những lần không đối xứng
    j = len(xau)-1
    for i in range(len(xau)):
        if xau[i] == xau[j]:
            so_buoc_bien_doi += 1
    # 
    return so_buoc_bien_doi

# nhập 1 xâu, tìm từ có len() max, không tính chữ số trong từ
def bai_5():        
    xau = input()

    chu_max = 0
    so_ky_tu_chu_cai_trong_chuoi = 0
    for i in xau:
        if i.isalpha():
            so_ky_tu_chu_cai_trong_chuoi += 1
        elif i == " ":
            if so_ky_tu_chu_cai_trong_chuoi > chu_max:
                chu_max = so_ky_tu_chu_cai_trong_chuoi
            so_ky_tu_chu_cai_trong_chuoi = 0
    if so_ky_tu_chu_cai_trong_chuoi > chu_max:
        chu_max = so_ky_tu_chu_cai_trong_chuoi
    print(chu_max)

bai_5()