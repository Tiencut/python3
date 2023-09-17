n= list(map(int,input().split()))

set_n = set(n)
tmp = 0
for i in set_n:
    if i % 5 == 0:
        tmp += i 
print(tmp)
