N = int(input())
# nhập
a = list(map(int, input().split()))
# 
namNhuan = 0
for i in range(N):
    if a[i] % 19 == 0 or a[i] % 19 == 3 or a[i] % 19 == 6 or a[i] % 19 == 9 or a[i] % 19 == 11 or a[i] % 19 == 14 or a[i] % 19 == 17:
        namNhuan+=1
# 
print(namNhuan)