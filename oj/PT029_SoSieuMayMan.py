# T = int(input())

# # số siêu may mắn: chỉ tồn tại 4 và 7, sl số 4 và 7 bằng nhau
# def SoSieuMayMan(n):
#     # check chỉ tồn tại số 4 và 7
#     # check sl số 4 và 7 = nhau
#     n = str(n)
#     slSo4 = slSo7 = 0
#     for i in n:
#         if i != "7" and i != "4":
#             return False
#         if i == "7":
#             slSo7 += 1
#         if i == "4":
#             slSo4 += 1
#     if slSo4 == slSo7:
#         return True
#     else:
#         return False

# for i in range(T):
#     n = int(input())
#     tmp = False
#     while not tmp:
#         if(SoSieuMayMan(n)):
#             print(n)
#             tmp = True
#         else:
#             n += 1

import bisect

# lưu all số siêu may mắn tìm được từ 4 và 7
soSieuMayMan = []

# tạo số siêu may mắn với 2 đối số sobon và sobay lần lượt là 4 và 7 trong số đó.
def timsoSieuMayMan(num, sobon, sobay):
    if num > 1e10:
        return
    if sobon == sobay:
        soSieuMayMan.append(num)
    timsoSieuMayMan(num * 10 + 4, sobon + 1, sobay)
    timsoSieuMayMan(num * 10 + 7, sobon, sobay + 1)

timsoSieuMayMan(0, 0, 0)
soSieuMayMan.sort()

T = int(input())
for i in range(T):
    n = int(input())
    idx = bisect.bisect_left(soSieuMayMan, n)
    print(soSieuMayMan[idx])
