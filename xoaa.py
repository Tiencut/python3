def cau_6():
    # tạo và ghi dữ liệu file SONNGUEN.INP
    with open("SONNGUYEN.INP","w") as f:
        f.write('34\n610')

    # Đọc data đầu vào từ file SONNGUYEN.INP
    with open("SONNGUYEN.INP","r") as f:
        A,B = f.readlines()
        A = A.strip()
        B = B.strip()

    # Tạo danh sách các chữ số của A,B
    digits_A = list(A)
    digits_B = list(B)

    # Tạo list các chữ số của Cmax (chèn đầu)
    digits_Cmax = digits_A + digits_B
    Cmax = int(''.join(digits_Cmax))

    A_str = ''.join(digits_A)
    for i in range(1,len(digits_B)):
        # Chèn chuỗi A vào vị trí thứ i của list B
        B_str = digits_B[:]
        B_str.insert(i, A_str)
        tmp = int(''.join(B_str))

        if tmp > Cmax:
            Cmax = tmp

    with open("SONNGUYEN","w") as f:
        f.write(str(Cmax))

cau_6()