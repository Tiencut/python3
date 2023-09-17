class SimpleClass:
    # Attribute: khai bao thuộc tính
    i=5
    # __init__: tạo đối tượng
    def __init__(self) -> None:
        self.i = 2
    # method: phươg thức (có 2 dạng phương thức: thông thường, method)
    def printMe(self):
        print(self.i)

class SimpleClass2:
    # constructor
    def __init__(self) -> None:
        self.name="tien cut"
    # method: muốn use phải có đối tượng
    def printHello(self):
        print(f"Hello {self.name}")
    # static methods
    @staticmethod
    def hi(name):
        print(f"hi {name}")


SimpleClass2.hi("tien")