n = int(input())

def check_chan(n):
    if n % 2 != 0:
        return True
    else:
        return False
    
def check_be_hon_0_and_chia_het_cho_3(n):
    if n > 0 and len(str(n)) == 3:
        return True
    else:
        return False

if check_chan(n) or check_be_hon_0_and_chia_het_cho_3(n):
    print("Yes")
else:
    print("No")