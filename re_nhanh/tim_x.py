# a.x+b=0
a,b = map(int,input().split())

# vô nghiệm
if a==0 and b!=0:
    print("No Solotuon")
# vô số nghiệm
elif a==0 and b==0:
    print("No Solotuon")
# 1 nghiệm
else:
    x = -b/a
    print("{:.2f}".format(x))