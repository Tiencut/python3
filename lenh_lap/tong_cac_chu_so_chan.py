T = int(input())

for i in range(T):
    n = input()
    tong_chu_so_chan = 0
    for i in n:
        if int(i) % 2 == 0:
            tong_chu_so_chan += int(i)
    print(tong_chu_so_chan)