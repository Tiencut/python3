n = int(input())

print('cac uoc so cua', n, 'la: ')
for i in range(1, n+1):
    if (n% i == 0):
        print(i, end=', ')