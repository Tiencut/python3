N = int(input())

A,B = map(int, input().split())

# ham sum cac chu so 
def TongCacChuSo(n):
    tmp = 0
    while (n>0):
        tmp += n%10
        n //= 10
    return tmp
# total: tổng
total = 0
# if sum cac chu so cua so do  = [A,B]
for i in range(1,N+1):
    if TongCacChuSo(i) >=A and TongCacChuSo(i) <= B :
        total += i

print(total)