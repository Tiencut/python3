class Sieu_nhan():
    power = 15
    def __init__(self,ten,tuoi) -> None:
        self.ten = ten
        self.tuoi = tuoi
        self.power += 1
    @staticmethod
    def tang_power(self):
        self.power += 1

sieu_nhan_A = Sieu_nhan("tien cut", 18)

print(sieu_nhan_A.power)