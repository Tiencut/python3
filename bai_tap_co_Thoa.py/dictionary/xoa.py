def bai_3():    
    n = int(input("n?"))

    SV = {}

    for i in range(n):
        masv = input("masv?:")
        diem_ktr = int(input("diem_ktr?"))
        SV[masv] = diem_ktr

    def chuyen_doi_diem(diem):
            if diem >= 8.5:
                return "A"
            elif diem >= 7:
                return "B"
            elif diem >= 5.5:
                return "C"
            elif diem >= 4:
                return "D"
            else:
                return "F"
            
    # in ds theo thang điểm 4 (A,B,C,D,F)
    for masv,diem in SV.items():
         print(f"{masv}:{chuyen_doi_diem(diem)}")

    # sắp xếp theo điểm giảm dần
    # x[0]:key, x[1]:value
    sorted_SV = sorted(SV.items(), key = lambda x:x[1], reverse=True)
    print("ds sv điểm giảm dần")
    for masv, diem in sorted_SV:
         print(f"{masv}:{diem}")

bai_3()