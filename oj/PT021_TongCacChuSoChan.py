# # # cach 1
# T = int(input())

# for j in range(T):
#     # 
#     N = int(input())
#     # 
#     if N < 0:
#         N = - N
#     # 
#     dem = 0
#     while N > 0:
#         tmp = N % 10
#         if (tmp % 2 == 0):
#             dem += tmp
#         N //= 10
#     # 
#     print(dem)

# # # cach 2
T = int(input())

for j in range(T):
    # khử dấu âm, chuyển về str
    N = str(abs(int(input())))
    # 
    dem = 0
    for i in N:
        if int(i) % 2 == 0:
            dem += int(i)
    # 
    print(dem)