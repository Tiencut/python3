a,b = map(int,input().split())
# a,b khac dau --> tich = 0
if (a >= 0 and b <= 0) or (a <= 0 and b >= 0):
    print("Zero")
# a,b > 0 -> tich > 0 
elif (a > 0 and b > 0):
    print("Positive")
# a,b < 0
else:
    # ct này không biết đâu ra kkk
    tmp = abs(abs(b) - abs(a)) + 1
    # 
    if tmp % 2 == 0:
        print("Positive")
    else:
        print("Negative")