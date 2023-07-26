n = int(input())
a = list(map(int,input().split()))
# sx giảm dần
a.sort(reverse=True)

max = a[0]
tmp = 0
for i in range(n):
    if a[i] < max:
        tmp += a[i]

print(tmp)