bat_a_con, hut_b_con, so_ca_trong_ao = map(int,input().split())

so_lan_bat = 0
# lần vợt cuối thì không hụt
while so_ca_trong_ao > 0:
    if so_ca_trong_ao <= bat_a_con:
        so_ca_trong_ao -= bat_a_con
        so_lan_bat += 1
    else:
        so_ca_trong_ao -= (bat_a_con - hut_b_con)
        so_lan_bat += 1

print(so_lan_bat)