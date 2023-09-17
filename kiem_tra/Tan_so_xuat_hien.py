list_input = list(map(int, input().split()))

list_input_sorted = sorted(list_input)
dem = 0
trung_gian = None

for i in list_input_sorted:
    if trung_gian == None:
        trung_gian = i
        dem = 1
    elif trung_gian == i:
        dem += 1
    else:
        print(dem,end=" ")
        trung_gian = i
        dem = 1

# in đếm của phần tử cuối
print(dem,end=" ")


# input:2 2 3 5 7
# output: 2 1 1 1