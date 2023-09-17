s = int(input("số thập phân? "))

def thap_sang_nhi(s):
    return str(bin(s))

r = thap_sang_nhi(s)
print(r[2:])