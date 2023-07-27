n = int(input())
import math
# phân tích 1 số thành các thừa số nguyên tố
def prime_factors(n):
    i = 2
    while n > 1:
        if n % i == 0:
            print(i, end=" ")
            n //= i
        else:
            i += 1
prime_factors(n)