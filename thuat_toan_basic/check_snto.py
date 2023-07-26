import math
def check_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(math.sqrt(n)):
        if n % i == 0:
            return False
    return True

def tim_uoc_chung_max_giua_hai_so(a,b):
    tmp = min(a,b)
    for i in range(tmp+1,1,-1):
        if a % i == 0 and b % i == 0:
            return i
    