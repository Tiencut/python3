n,p,q = map(int,input().split())

for i in range(1,n+1):
    if (i % p == 0) or (i % q == 0):
        print(i,end=" ")