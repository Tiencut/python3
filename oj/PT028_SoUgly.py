n = int(input())

def SoUgly(n):
    while n%2 == 0:
        n //= 2
    while n%3 == 0:
        n //= 3
    while n%5 == 0:
        n //= 5

    if n == 1:
        return True
    else:
        return False

if(SoUgly(n)):
    print("YES")
else:
    print("NO")
