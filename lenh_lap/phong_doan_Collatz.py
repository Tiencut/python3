# n lẻ, n > 1 --> 3*n+1
# n chẵn n//=2
n = int(input())

day_Hailstone = []
while n != 1:
    day_Hailstone.append(n)
    if n % 2 == 0:
        n //= 2
    elif n % 2 != 0 and n > 1:
        n = 3*n+1
    if n == 1:
        day_Hailstone.append(n)
        break

print(len(day_Hailstone))