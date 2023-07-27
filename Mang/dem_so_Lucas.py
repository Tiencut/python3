from math import *

n = int(input())
a = list(map(int,input().split()))

so_Lucas = 0

def check_so_Lucas(so_can_check):
    if so_can_check == 2:
        return True
    a = 2
    b = 1
    while b < so_can_check:
        c = a + b
        a = b
        b = c
        if b == so_can_check:
            return True
    return False

for i in range(n):
    if(check_so_Lucas(a[i])):
        so_Lucas += 1
    
print(so_Lucas)