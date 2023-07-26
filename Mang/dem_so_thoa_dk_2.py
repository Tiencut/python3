n = int(input())
a = list(map(int,input().split()))

def check_chan_or_chia_het_cho_3_or_5_and_co_3_chu_so(a):
    tmp = 0
    for i in a:
        i = abs(i)
        if (i % 2 == 0): 
            tmp += 1
            continue
        if( (i%3 == 0 or i%5 == 0) and (len(str(i)) == 3) ):
            tmp += 1
    return tmp

print(check_chan_or_chia_het_cho_3_or_5_and_co_3_chu_so(a)) 

