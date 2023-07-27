from math import *

a,b,alpha = map(float, input().split())
pi = 3.14159
S = 0.5*a*b*sin(alpha*pi/180)
print('%.4f'%S)