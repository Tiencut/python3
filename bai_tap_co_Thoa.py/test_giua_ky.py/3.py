s = list(map(int,input().split()))

def a(s):    
    print(s.count(0))
    print(s.count(1))

def b(s):
    s = sorted(s,reverse=True)
    print(s)

b(s)