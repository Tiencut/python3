from math import *

n = int(input())
tienCut=1
if n>=-1 and n<=30:
    if n == 0 or n == 1:
        print(1)
    # chan
    elif n%2==0:
        for i in range(2,n+1,2):
            tienCut*=i
        print(tienCut)
    # le
    if n%2!=0:
        for i in range(3,n+1,2):
            tienCut*=i
        print(tienCut)