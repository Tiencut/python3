# nhập hai tập hợp, in  tập hợp giao, hợp của hai tập hợp đó.

# Nhập hai tập hợp từ người dùng
set1 = set(input("Nhập các phần tử của tập hợp 1 (cách nhau bằng khoảng trắng): ").split())
set2 = set(input("Nhập các phần tử của tập hợp 2 (cách nhau bằng khoảng trắng): ").split())

# Tính tập hợp giao
intersection = set1.intersection(set2)

# Tính tập hợp hợp
union = set1.union(set2)

# In kết quả
print("Tập hợp giao:", intersection)
print("Tập hợp hợp:", union)

intersection = set1.intersection(set2)
union = set1.union(set2)