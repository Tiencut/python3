n = int(input())
a = list(map(int, input().split()))

so_am = so_duong = so_chan = so_le = 0

for i in range(n):
    # 
    if a[i] < 0:
        so_am += 1
    elif a[i] > 0:
        so_duong += 1
    # 
    if abs(a[i]) % 2 == 0:
        so_chan += 1
    else:
        so_le += 1

print(so_am)
print(so_duong)
print(so_chan)
print(so_le)
