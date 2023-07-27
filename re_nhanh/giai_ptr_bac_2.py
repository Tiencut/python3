import math
# giải ptr ax^2+bx+c=0 (a khác 0)
a,b,c = map(float,input().split())

delta = b**2 - 4*a*c
# có nghiệm
if delta < 0:
    print("No Solution")
# vô nghiệm
elif delta == 0:
    x = -b/2*a
    print(x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("{:.4f}\n{:.4f}".format(x1,x2))