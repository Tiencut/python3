N = int(input())

# ham sum cac chu so 
def TongCacChuSo(n):
    tmp = 0
    while (n>0):
        tmp += n%10
        n //= 10
    if tmp%10 == 9:
        return 1
    else:
        return 0

dem = 0
for i in range(1,N+1):
    if TongCacChuSo(i):
        dem += 1

print(dem)