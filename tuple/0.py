# tuple, cấu trúc data không thay đổi

# # khởi tạo
# my_tuple = (1,2,3)
# # or
# another_tuple = tuple([4,5,6])
# print(my_tuple, another_tuple)

# my_tuple = (1,2,3)
# print(my_tuple[0])

# k đổi gtr sau khi tạo
# my_tuple = (1,2,3)
# my_tuple[0] = 2

# unpacking tuple
# my_tuple = (1,2,3)
# a,b,c = my_tuple
# print(a,b,c)

# use tuple làm key trong dictionary
my_dict = {(1,2) : "value"}
print(my_dict[(1,2)])