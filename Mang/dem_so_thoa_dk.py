n = int(input())
a = list(map(int,input().split()))

tmp = 0
for i in range(n):
    if (a[i] % 2 == 0) or (a[i] < 0 and a[i] % 3 == 0):
        tmp += 1    

print(tmp)