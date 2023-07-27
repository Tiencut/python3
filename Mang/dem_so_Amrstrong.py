n = int(input())
a = list(map(int,input().split()))

so_Amstrong = 0

def dem_so_Amstrong(so_can_check):
    tmp = 0
    so_luong_chu_so = len(str(so_can_check))
    for j in str(so_can_check):
        tmp += int(j)**so_luong_chu_so
    
    if tmp == so_can_check:
        return True
    else:
        return False

for i in range(n):
    if(dem_so_Amstrong(a[i])):
        so_Amstrong += 1
    
print(so_Amstrong)