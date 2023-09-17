m,n = map(int,input().split())

L = [ [ int(input()) for col in range(n)] for row in range(m)]

print(L)

def sum_duong_bien(m,n,L):
    tren = sum( [L[0][col] for col in range(n)] )
    duoi = sum( [L[m-1][col] for col in range(n)] )
    trai = sum( [L[row][0] for row in range(1,m-1)] )
    phai = sum( [L[row][n-1] for row in range(1,m-1)] )

    print("tổng đường biên",tren+duoi+trai+phai)

def vtr_ptu_max(m,n,L):
    vtr_ptu_max_first = max(L)
    # for row in range(m):
    #     for col in range(n):
    #         if L[row][col] > vtr_ptu_max_first:
    #             vtr_ptu_max_first = L[row][col]
    print(vtr_ptu_max_first)

sum_duong_bien(m,n,L)
vtr_ptu_max(m,n,L)