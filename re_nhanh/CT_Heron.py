# công thức heron
a,b,c = map(float,input().split())

# nửa chu vi
p = (a+b+c)/2

# vô nghiệm
if a+b <=c or a+c<= b or b+c <= a:
    print("No Solution")
else:
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print("{:.4f}".format(S))