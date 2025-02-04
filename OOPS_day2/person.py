class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def getInfo(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.id}")


class Employee(Person):
    def __init__(self, name, age, id, salary):
        self.salary = salary
        super().__init__(name, age, id)

    def dsp(self):
        print(super().getInfo(), self.salary)


e = Employee('Ravi', 30, 1001, 50000)
e.getInfo()
e.dsp()
