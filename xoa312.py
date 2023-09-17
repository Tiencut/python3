from math import*

def ts(s):
    so = 0
    dem = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            so = so * 10 + int(s[i])  
        elif so > 0:
            dem += 1
            so = 0 
    if so > 0:
      dem += 1
    print(dem)

s = input()
ts(s)