class Dog:
    __name = ''
    name = ''

    def setName(self,name):
        self.__name = name

    def showName(self):
        print(self.__name)

d = Dog()

# sai --> __name ở mức private
d.__name = "Su"

d.__name = "Đốm"

# đúng --> setName là public
d.setName(d.name)

# đúng --> showName là public
d.showName()