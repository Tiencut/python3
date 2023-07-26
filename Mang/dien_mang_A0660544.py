A = [1] 
n = 2
while len(A) < 100001:
    T_n_2 = n * (n - 1) // 2
    A.append(T_n_2)
    n += 3

k = abs(int(input()))
print(A[k])