S = input()
N = int(input())
xi = list(map(int,input().split()))

for i in range(N):
    for j in range(xi[i]):
        print(S,end="")
    print()