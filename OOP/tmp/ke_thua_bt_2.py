class Person:
    def __init__(self,name,age,gender) -> None:
        self.name = name        
        self.age = age   
        self.gender= gender   

    def print_in4(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")

class Employee(Person):
    def __init__(self, name, age, gender, job_title, salary) -> None:
        super().__init__(name, age, gender)
        self.job_title = job_title
        self.salary = salary

    def print_in4(self):
        super().print_in4()
        print(f"job_title: {self.job_title}")
        print(f"salary: {self.salary}")

employee = Employee("tien cut", 30, "male", "software Engineer", 10000)
employee.print_in4()