# class Engine:
#     a = 10

#     def __init__(self):
#         self.b = 20

#     def m1(self):
#         print(self.a)


# class Car:
#     def __init__(self):
#         self.engine = Engine()

#     def m2(self):
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()


# c = Car()
# c.m2()

class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def display(self):
        print(f"Name: {self.name}, Model: {self.model}, Color: {self.color}")


class Employee:
    def __init__(self, name, id, car):
        self.name = name
        self.id = id
        self.car = car  # car should be an instance of Car class

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.id}")
        self.car.display()


c = Car('BMW', 'X5', 'Black')
e = Employee('Ravi', 1001, c)
e.display()
