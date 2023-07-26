# viết hàm first_diff
# trả về vị trí đầu tiên 2 chuỗi khác nhau
# nếu 2 chuỗi giống nhau trả về -1
# viết hàm ở 2 dạng đệ quy và không đệ quy
def first_diff_de_quy(s1,s2):
    if s1 == s2:
        return -1
    lenght = min((s1),len(s2))
    for i in range(lenght):
        if s1[i] != s2[i]:
            return i
    return lenght

s1 = input("s1: ")
s2 = input("s2: ")

print(f"s1:{s1}")
print(f"s2:{s2}")

print(first_diff_de_quy(s1,s2))