import math
# Hàm ktr snt 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
# Hàm tính sl ước số dương của một thừa snt trong n!
def count_divisors(n, prime):
    total = 0
    while n >= prime:
        total += n // prime
        n //= prime
    return total
# 
n = int(input())
MOD = 10**9 + 7
# divisors_count: 
# sl các ước số dương của all thừa snt trong n! đến thời điểm hiện tại
divisors_count = 1
for i in range(2, n+1):
    if is_prime(i):
        divisors_count = (divisors_count * (count_divisors(n, i) + 1)) % MOD

print(divisors_count)