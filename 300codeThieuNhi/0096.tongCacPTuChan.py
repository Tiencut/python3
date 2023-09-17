n = int(input())
n_list = list(map(int,input().split()))

def Sum_ptu_chan():
    tong_chan = []
    for i in n_list:
        if i % 2 == 0:
            tong_chan.append(i)

    if len(tong_chan) == 0:
        return 0
    return sum(tong_chan) / len(tong_chan)

print('%.2f' % Sum_ptu_chan())