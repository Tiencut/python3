T = int(input())

def namNhuan(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    return False

for i in range(T):
    n = int(input())
    if namNhuan(n):
        print("leap year")
    else:
        print("none")