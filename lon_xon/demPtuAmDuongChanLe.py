T = int(input())

for i in range(T):
    dem = 0
    N = input()
    for i in N:
        if int(i) % 2 == 0:
            dem += int(i)
    print(dem)