n = int(input())
n_list = map(input().split())

for x in n_list:
    print(f"{x*x} ",end="")

del n_list