n = input()
# cach 1
# try:
#     m = int(n)
#     print(type(m))
# except ValueError:
#     try:
#         m = float(n)
#         print(type(m))
#     except ValueError:
#         print("kieu data khong la number")
# cach 2: use function digit
if n.isdigit():
    print('so')
else:
    print('chuoi')