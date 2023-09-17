class Xe:
    def __init__(self) -> None:
        print("hàm khởi tạo lớp cha")

class XeDap(Xe):
    def __init__(self) -> None:
        super().__init__()

d = XeDap()