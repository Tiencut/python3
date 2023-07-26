# ước số of n là những số n chia hết cho chúng
n = int(input())

uoc_so = []
for i in range(1,n+1):
    if n % i == 0:
        uoc_so.append(i)

print(len(uoc_so))

for i in uoc_so:
    print(i,end=" ")