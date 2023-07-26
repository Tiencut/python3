
M = [ [j for j in range(5)] for i in range(10)]
n = len([number for row in M for number in row if number % 2 == 0])

print(M)
print(n)