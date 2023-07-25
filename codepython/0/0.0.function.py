import numpy as np

# a = np.array([1,3,6])
# print(a)

# a2 = np.array([[1,2,3], [4,5,6]])
# print(a2)

# a3 = np.array([ [[1,2,3], [4,5,6]],
#                [[1,2,3], [4,5,6]],
#                [[1,2,3], [4,5,6]] ])
# print(a3)

# import random
# tmp = [ [ [ random.randint(0,10) for k in range(4) ] for j in range(2)] for i in range(3) ]
# a3 = np.array(tmp)
# print(a3)

# shape: số cột-dòng
a5 = np.array([1,2,3,4])
print(a5)
print(f"kích thước mảng: {a5.shape}")
print(f"số chiều của mảnh: {a5.ndim}")
print(f"kiểu data: {a5.dtype}")
print(f"số phần tử: {a5.size}")
