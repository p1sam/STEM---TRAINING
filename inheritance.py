class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def details(self):
        print(f"My name is {self.name} and my age is {self.age}")

p1 = Person("Sam", 18)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary
    def details(self):
        print(f"My name is {self.name} i earn{self.salary}")

p2 = Employee("John", 22, 500)
p2.details()