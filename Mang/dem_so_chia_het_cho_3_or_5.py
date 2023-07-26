from math import *

n = int(input())
a = list(map(int,input().split()))

so_chia_het_cho_3_or_5 = 0

def dem_so_chia_het_cho_3_or_5(so_can_check):
    if so_can_check % 3 == 0 or so_can_check % 5 == 0:
        return True
    else:
        return False

for i in range(n):
    if(dem_so_chia_het_cho_3_or_5(a[i])):
        so_chia_het_cho_3_or_5 += 1
    
print(so_chia_het_cho_3_or_5)