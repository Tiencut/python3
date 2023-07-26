Q = int(input())

def calculate_digit_sum(number):
    digit_sum = 0
    
    while number > 0:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum

for _ in range(Q):
    L, R = map(int, input().split())
    total_sum = 0
    
    for i in range(L, R + 1):
        total_sum += calculate_digit_sum(i)
    
    print(total_sum)