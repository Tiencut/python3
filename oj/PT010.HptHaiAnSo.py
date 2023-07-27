from math import *

T = int(input())
for i in range(T):
    a1,b1,c1,a2,b2,c2 = map(float, input().split())
    
    D=(a1*b2)-(a2*b1)
    Dx=float((b2*c1)-(b1*c2))
    Dy=float((a1*c2)-(a2*c1))
    
    if D == 0:
        if Dx + Dy == 0:
            print("Many solutions")
        else:
            print("No Solution")
    else:
        x=Dx/D
        y=Dy/D
        
        print('%.6f'%x + " " + '%.6f'%y)