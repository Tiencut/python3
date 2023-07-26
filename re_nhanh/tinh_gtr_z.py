x = int(input())

if x >= 0:
    z = x**3 + 2*x**2 + 4*x - 6
elif x < 0:
    z = x**3 - 7*x

print(z)