n = int(input())

for i in range(2*n+1):
    for j in range(2*n+1):
        if i == j or i + j == 2*n:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()