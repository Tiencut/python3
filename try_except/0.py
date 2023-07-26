# try:
#     # đoạn code dự đoán có lỗi
# except:
#     # hđ khi lỗi xra
# else:
#     # thực thi đoạn này nếu như mã k lỗi
# finally:
#     # cho phếp thực thi mã, bất kể lỗi hay không

try:
    a = int(input("nhập số nguyên: "))
    print(a)
except:
    print("nhập sai kiểu data, nhập lại đi ạ!")
else:
    print("k lỗi xra")
finally:
    print("end program")