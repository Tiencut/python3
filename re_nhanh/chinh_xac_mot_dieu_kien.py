n = int(input())

def check_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def check_be_hon_0_and_chia_het_cho_3(n):
    if n < 0 and n % 3 == 0:
        return True
    else:
        return False

# chỉ thoả 1 trong 2 đk
chi_thoa_1_trong_2_dk = False
if check_chan(n) and check_be_hon_0_and_chia_het_cho_3(n):
    print("No")
elif check_chan(n) or check_be_hon_0_and_chia_het_cho_3(n):
    print("Yes")
else:
    print("No")