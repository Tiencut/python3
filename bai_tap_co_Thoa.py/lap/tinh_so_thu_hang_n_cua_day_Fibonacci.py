n = int(input())

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) (với n ≥ 2)
def fibonacci_ppDeQuy(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_ppDeQuy(n-1) + fibonacci_ppDeQuy(n-2)
def fibonacci_ppVongLap(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(3,n + 1):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci_ppVongLap(n))
# 0 1 1 2 3 5 8 13
# n = 3