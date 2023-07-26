N = int(input())
# nhập
a = list(map(int, input().split()))
#
tien_cut = [0,3,6,9,11,14,17]
namNhuan = sum( a[i] % 19 in tien_cut for i in range(N))
# 
print(namNhuan)