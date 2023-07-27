from math import *
x1,y1,x2,y2 = map(float,input().split())

d = sqrt((x2-x1)**2 + (y2-y1)**2)
d = round(d,9)

print("{:.9f}".format(d))
