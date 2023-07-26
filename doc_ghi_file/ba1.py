# đọc nội dung của file file.txt, ghi nội dung đã đọc vào file file2.txt.
f = open("file.txt","x")

if not os.path.exist("file.txt"):
    print("file khong ton tai")
    exit()

f = open("file.txt","r")
content = f.read()
f.close()

f1 = open("file2.txt","w")
f1.write(content)
f1.close()

f2 = open("file2.txt","r")
f2.read()
f2.close()