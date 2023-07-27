from math import *
a,b,c = map(float, input().split())
p = (a+b+c)/2
if a>=b+c or b>=a+c or c>=a+b or a<=0 or b<=0 or c<=0:
    print("No Solution")
else:
    print("%.6f"% ( sqrt( p*(p-a)*(p-b)*(p-c) ) ) )