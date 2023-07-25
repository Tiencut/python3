import numpy as np

# truy cập bằng index
# x1 = np.random.randint(10,size=6)
# print(x1)
# print(x1[1],x1[0])
# print(f"cách truy cập phần tử cuối: {x1[-1]}")

# x2 = np.random.randint(10,size=(2,3))
# print(x2)
# print("x2 [0,1] = ",x2[0,1])
# # có thể thay đổi giá trị bằng truy cập index
# x2[0,1] = 10
# print(x2)

# SLICING
# x[start:stop:step]
# x3 = np.random.randint(10,size=5)
# print(x3)
# print(f"3 element đầu: {x3[0:3]}")

# 
x4 = np.random.randint(10,size=(2,3))
print(x4)
# :1 để nói hàng số mấy? start=1
# :2 để nói cột số mấy? start=1
print()
print(x4[:1,:2])
print()
print(x4[:,:2])