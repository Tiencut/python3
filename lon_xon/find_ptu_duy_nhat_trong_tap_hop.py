# # Nhập danh sách từ người dùng
# my_list = input("Nhập các phần tử của danh sách (cách nhau bằng khoảng trắng): ").split()

# # Tạo một set từ danh sách để loại bỏ các phần tử trùng lặp
# unique_set = set(my_list)

# # In kết quả
# print("Các phần tử duy nhất:", unique_set)

# Tạo một tập hợp từ danh sách
my_set = set([1, 2, 3, 4, 5])

# Chuyển đổi tập hợp thành danh sách
my_list = list(my_set)

# In kết quả
print("Danh sách:", my_set)
print("Danh sách:", my_list)
