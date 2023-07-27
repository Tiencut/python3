n = int(input())
a = list(map(int,input().split()))

so_chia_het_cho_3_or_5 = 0
for i in a:
    if i % 3 == 0 or i % 5 == 0:
        so_chia_het_cho_3_or_5 += 1

print(so_chia_het_cho_3_or_5)