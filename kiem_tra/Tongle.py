n = int(input())

def Tong_le(n):
    Tong_le = 0
    for i in range(1,n+1,2):
        Tong_le += i
    return Tong_le

print(Tong_le(n))