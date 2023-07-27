x = int(input())

Y = 0

if x > 3:
    Y = x**3 + 2*x**2 + 5*x
elif x <= 3 and x >= 1:
    Y = x**2 - 2*x + 4
else:
    Y = 5*x - 8

print(Y)