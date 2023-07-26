import math
# n khách, p khoang(4 chỗ)
n,p = map(float,input().split())

so_toa = math.ceil( n / (4*p) )
print(so_toa)