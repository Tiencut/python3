class Animals:
    # constructor: build đối tượng
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print(f"my name is {self.name}")

class Dog(Animals):
    def bark(self):
        print("Woof!")

class Cat(Animals):
    def bark(self):
        print("Meow!")

dog1 = Dog("Su")
dog1.speak()
dog1.bark()
# dog1.printMe()