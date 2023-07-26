def sum_digits(num):
    num = str(num)
    tmp = 0
    for i in num:
        tmp += int(i)
    return tmp

print(sum_digits(num=121))

# def del_negative(list_tien_cut):
#     new_list = []
#     for i in range(len(list_tien_cut)):
#         if list_tien_cut[i] >= 0:
#             new_list.append(list_tien_cut[i])

#     return new_list

# # list_tien_cut = [1,-1,2]
# # print(del_negative(list_tien_cut))
# # print(list_tien_cut)
# import math
# def comb_tien(n,k):
#     return comb(n,k)