s = input()

# ktr chuỗi đối xứng không
def ktr_string_doi_xung(s):
    s_reverse = s[::-1]
    return s == s_reverse

def so_buoc_dua_xau_ve_doi_xung(s):
    dau_chuoi = 0
    cuoi_chuoi = len(s)-1
    count = 0

    while dau_chuoi < cuoi_chuoi:
        if s[dau_chuoi] != s[cuoi_chuoi]:
            count += 1

        dau_chuoi += 1
        cuoi_chuoi -= 1

    return count

def xoa_ki_tu_duoc_nhap_tu_ban_phim(s):
    xau_sau_khi_xoa = ""

    for i in s:
        if i == ki_tu_muon_xoa:
            continue
        else:
            xau_sau_khi_xoa += i

    return xau_sau_khi_xoa

if ktr_string_doi_xung(s):
    print("chuoi doi xung")
else:
    print("chuoi khong doi xung")
    # cần bao nhiêu bước để đưa xâu về đối xứng
    so_buoc_de_dua_xau_ve_doi_xung = so_buoc_dua_xau_ve_doi_xung(s)
    print("so buoc de dua chuoi ve doi xung",so_buoc_de_dua_xau_ve_doi_xung)

print()
ki_tu_muon_xoa = input("ki tu muon xoa: ")
print(f"\nki tu sau khi xoa: {xoa_ki_tu_duoc_nhap_tu_ban_phim(s)}")