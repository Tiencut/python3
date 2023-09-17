# nhập họ tên, in ra họ và họ đệm
# ho_ten = input()
def inth(ho_ten):
    # strip(): lược bỏ dầu cách thừa đầu và cuối
    ho_ten_list = ho_ten.split()
    print( ' '.join( ho_ten_list[:(len(ho_ten_list) - 1)]) )

inth("    duong    chi    phu   ")