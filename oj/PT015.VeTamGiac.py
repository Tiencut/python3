T = int(input())
if T<=100:
    for i in range(T):
        n = int(input())
        # nữa trên
        for i in range(1,n+1):
            for j in range(i):
                print('* ', end='')
            print()
        # nữa dưới
        for i in range(n-1,0,-1):
            for j in range(i):
                print('* ', end='')
            print()