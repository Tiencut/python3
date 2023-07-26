# hai lớp: Animal và Dog. 
# Animal có các thuộc tính name và age, và phương thức speak(). Phương thức speak() in ra tên của con vật. 
# Dog kế thừa từ lớp Animal, và có thêm thuộc tính breed. 
# tạo một đối tượng Dog mới, gán tên và giống cho đối tượng, và gọi phương thức speak().
class Animal:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age= age
    
    def speak():
        print("kêu tiếng gì đó")

class Dog(Animal):
    def __init__(self, name, age,breed) -> None:
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("chó sủa Gâu Gâu")

dog = Dog("Su",10,"lùn")
dog.speak()