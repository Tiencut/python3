def sxMaTran():
    m,n = map(int,input().split())
    L = []
    for row in range(m):
        tmp = list(map(int,input().split()))
        L.append(tmp)
    
    L = sorted(L)
    print(L)

sxMaTran()