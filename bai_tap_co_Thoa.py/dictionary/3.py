def bai_3():  
    def input_n_sv():
        n = int(input("sl sv sẽ nhập? "))
        ds_sv = {}
        for i in range(n):
            masv = input("masv? ")
            diem = float(input("diem? "))
            ds_sv[masv] = diem
        return ds_sv
    
    def chuyen_doi_diem(diem):
            if diem >= 9:
                return "A"
            elif diem >= 8:
                return "B"
            elif diem >= 7:
                return "C"
            elif diem >= 5:
                return "D"
            else:
                return "F"
    
    def in_ds_sv_thang_diem_4(ds_sv):    
        for masv, diem in ds_sv.items():
            print(f"masv: {masv}, diem: {chuyen_doi_diem(diem)}")
    
    def in_sv_diem_giam_dan(ds_sv):
        sorted_ds = sorted(ds_sv.items(),key=lambda x: x[1],reverse=True)
        for masv, diem in sorted_ds:
            print(f"masv: {masv}, diem: {ds_sv[masv]}")
    # nhập ds sv
    ds_sv = input_n_sv()
    # in ds theo thang điểm 4
    in_ds_sv_thang_diem_4(ds_sv)
    # in ds điểm giảm dần
    in_sv_diem_giam_dan(ds_sv)

bai_3()