#  đọc in4  file văn bản và in ra màn hình.
file = open("file.txt","r")
content = file.read()
print(content)
file.close()