n = int(input())

for a in range(1, 201):
    if a != n:
        b = (a * n) // (a - n)
        if 1<=b<=200 and (a*b) == (a+b)*n:
            print(a,b)