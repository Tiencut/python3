# # n phai la so nguyen duong
# n = abs(int(input()))
# # 
# a = str(n)
# chuSoChan = 0
# for i in a:
#     # chan
#     if int(i)%2==0:
#         chuSoCha  
#         n += 1

# print(chuSoChan)

n = abs(int(input()))

chuSoLe = 0
while n>0:
    # chan
    if n%2!=0:
        chuSoLe += 1
    n = n // 10

print(chuSoLe)