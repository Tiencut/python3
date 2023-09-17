class ngay:
    def __init__(self, gtri_ngay, gtri_thang, gtri_nam):
        self.ngay = gtri_ngay
        self.thang = gtri_thang
        self.nam = gtri_nam

    @staticmethod
    def SoNgayCuaThang(thang,nam):
        if(thang in [1,3,5,7,8,10,12]):
            return 31
        elif thang in [4,6,9,11]:
            return 30
        elif thang == 2:
            return 29 if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0) else 28
        
    def ngayTrongNam(self):
        gtri_ngay_trong_nam = 0
        
        for i in range(1,self.thang):
            gtri_ngay_trong_nam += self.SoNgayCuaThang(i,self.nam)
        gtri_ngay_trong_nam += self.ngay

        return gtri_ngay_trong_nam
    
ngayA = ngay(15,3,2022)
print(ngayA.ngayTrongNam())