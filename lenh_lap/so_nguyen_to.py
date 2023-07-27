import math
n = int(input())

def check_so_nguyen_to(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

if check_so_nguyen_to(n):
    print("Yes")
else:
    print("No")