from math import *

n = int(input())
a = list(map(int,input().split()))

so_chinh_phuong = 0

def check_so_chinh_phuong(so_can_check):
    if int(sqrt(so_can_check))**2 == so_can_check:
        return True
    else:
        return False

for i in range(n):
    if(check_so_chinh_phuong(a[i])):
        so_chinh_phuong += 1
    
print(so_chinh_phuong)