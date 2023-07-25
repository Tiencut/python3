import numpy as np
import math

def use_code_tinh_vector():
    # nhập tọa độ
    x1,y1,z1 = map(float,input("nhập tọa độ vector1: ").split())
    x2,y2,z2 = map(float,input("nhập tọa độ vector2: ").split())

    # tích vô hướng
    tich_vo_huong_tu = (x1*x2 + y1*y2 + z1*z2)
    print(tich_vo_huong_tu)
    print(f"tích vô hướng 2 vector = {tich_vo_huong_tu}")

    mau = math.sqrt(x1**2 + y1**2 +z1**2) * math.sqrt(x2**2 + y2**2 +z2**2)
    
    # gốc giữa 2 vector
    ct_cos = tich_vo_huong_tu/mau
    print(f"gốc giữa 2 vector(đơn vị: độ) = {math.degrees(math.acos(ct_cos))}")

    # hình chiếu của vector này lên vector kia
    hinh_chieu_tu = x2*x1 + y2*y1 + z2*z1
    hinh_chieu_mau = (math.sqrt(x1**2 + y1**2 + z1**2))**2
    hinh_chieu = hinh_chieu_tu/hinh_chieu_mau

    print(f"hình chiếu = {hinh_chieu}")

use_code_tinh_vector()

def use_numpy_tinh_vector():
    vector1 = np.array(input("Nhập tọa độ vector 1: ").split(), dtype=float)
    vector2 = np.array(input("Nhập tọa độ vector 2: ").split(), dtype=float)

    dot_product = np.dot(vector1, vector2)
    print(dot_product)
