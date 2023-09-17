def t():
    # tạo và ghi dữ liệu file SONNGUEN.INP
    with open("SONNGUYEN.INP","w") as f:
        f.write('34\n610')

    # Đọc data đầu vào từ file SONNGUYEN.INP
    with open("SONNGUYEN.INP","r") as f:
        lines = f.readlines()
        A = lines[0].strip()
        B = lines[1].strip()

t()