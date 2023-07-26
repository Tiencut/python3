chuoi_tu_user = input().split()
chuoi_tu_user = map(input().split())
so_lan_xuat_hien_cua_tung_tu = {}

for tu in chuoi_tu_user:
    if tu in so_lan_xuat_hien_cua_tung_tu:
        so_lan_xuat_hien_cua_tung_tu [tu] += 1
    else:
        so_lan_xuat_hien_cua_tung_tu[tu] = 1

for tu,so_lan in so_lan_xuat_hien_cua_tung_tu.items():
    print(f"{tu}:{so_lan}")