from math import *

n = int(input())
a = list(map(int,input().split()))

so_nguyen_to = 0

def check_so_nguyen_to(so_can_check):
    if so_can_check < 1:
        return False
    for i in range(1,int(sqrt(so_can_check))):
        if so_can_check%i:
            return False
    return True

for i in range(n):
    if(check_so_nguyen_to(a[i])):
        so_nguyen_to += 1
    
print(so_nguyen_to)