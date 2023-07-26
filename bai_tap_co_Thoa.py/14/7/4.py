# nhị phân sang thập phân
nhi_phan = input()

def nhi_phan_sang_thap_phan(nhi_phan):
    thap_phan = 0
    tmp = len(nhi_phan)-1

    for i in range(len(nhi_phan)):
        thap_phan += int(nhi_phan[i]) * (2**tmp)
        tmp -= 1

    return thap_phan

def ham_co_san(nhi_phan):
    thap_phan1 = int(nhi_phan,2)
    return thap_phan1

print(nhi_phan_sang_thap_phan(nhi_phan))