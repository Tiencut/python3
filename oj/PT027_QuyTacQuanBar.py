N = int(input())

loaiRuouBiCam = {"ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"}
soNguoiViPham = 0

for i in range(N):
    n = input()
    if n.upper() in loaiRuouBiCam:
        soNguoiViPham += 1
    elif n.isdigit() and (int(n) < 18 and int(n) != 16):
        soNguoiViPham += 1

print(soNguoiViPham)

# n = int(input())
# dem = 0
# drink = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]

# for i in range(n):
#     s = input()
#     if s.isdigit():
#         so = int(s)
#         if so < 18 and so != 16:
#             dem += 1
#     else:
#         if s in drink:
#             dem += 1

# print(dem)
