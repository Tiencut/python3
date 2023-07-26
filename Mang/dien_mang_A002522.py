A = []
for i in range(10001):
    A.append(i**2+1)

k = abs(int(input()))
print(A[k])