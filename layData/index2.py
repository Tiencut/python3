
# input:https://student.husc.edu.vn/Course/Details/2023-2024.1.TIN3042.009/
# output:https://student.husc.edu.vn/Course/Details/2023-2024.1.TIN3042.0

# link_nhap = input("link? ")
link_nhap = "https://student.husc.edu.vn/Course/Details/2023-2024.1.TIN3042.009/"
link_nhap = link_nhap[:-3]
print(link_nhap)


ls = []
for i in range(25):
    if i<10:
        ls.append(link_nhap + str(0) + str(i) + '/')
    else:
        ls.append(link_nhap + str(i) + '/')
for link in ls:
    print(link)


