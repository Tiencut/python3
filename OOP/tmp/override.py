class Parent():
 
    def show(self):
        print("Cha")
 
class Child(Parent):
    def show(self):
        print("Con")
 
class GrandChild(Child):
    def show(self):
        Parent.show(self)
        print("Cháu")
 
# Chương trình chính
g = GrandChild()
g.show()