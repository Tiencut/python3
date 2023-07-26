n = int(input())

# 
gio = n // 3600
n = n - gio*3600
phut = n // 60
n = n- phut*60
giay = n 

print("{:02d}:{:02d}:{:02d}".format(gio,phut,giay))