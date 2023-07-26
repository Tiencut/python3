# đọc file -> sử dụng phương thức open(). 
# có hai tham số: tên file và chế độ. 

# Chế độ:
# "x": tạo file
try:
    f = open("xoa.txt","x")
except Exception as e:
    print(e)
finally:
    f.close()

# "r":(read) đọc file, 
try:
    with open("xoa.txt","r") as f:
        # noi_dung = f.read()
        # print(noi_dung)
        list_noi_dung = f.readline()
        for i in list_noi_dung:
            print(i)
except Exception as e:
    print(e)
finally:
    f.close() 


# "w":(write) ghi file, 
# try:
#     with open("xoa.txt","w") as f:
#         f.write("xin chao.")
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# # "a": thêm nội dung vào file
# try:
#     with open("xoa.txt","a") as f:
#         f.write("xin chao.")
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# "rb": đọc file định dạng nhị phân.

# mở file, 
# read(): đọc nội dung file (dạng chuỗi chứa nội dung của file) 
# readline(): đọc từng dòng file (trả một chuỗi chứa một dòng của file)

# Để ghi file sử dụng phương thức write(). 
# Phương thức  có một tham số là nội dung cần ghi vào file.

# Sau khi ghi file, sử dụng  close() để đóng file. 
# giải phóng tài nguyên của file.

# ví dụ về cách đọc file trong Python:


# 
# f = 
f = open("xoa1.txt", mode="w", encoding="urf-8")