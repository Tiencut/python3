n = input()

def check_so_armstrong(n):
    tmp = 0
    for i in n:
        tmp += int(i)**len(n)
    return tmp == int(n)

if check_so_armstrong(n):
    print("Yes")
else:
    print("No")
