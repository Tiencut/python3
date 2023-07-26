def day_Fibonacci_cach_de_quy(n):
    if n == 0 or n == 1:
        return n
    elif n>1:
        return day_Fibonacci_cach_de_quy(n-1) + day_Fibonacci_cach_de_quy(n-2)

def day_Fibonacci_khong_de_quy(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>1:
        a = 0
        b = 1
        c = a + b
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return c

n = 5
print(day_Fibonacci_cach_de_quy(n))
print(day_Fibonacci_khong_de_quy(n))