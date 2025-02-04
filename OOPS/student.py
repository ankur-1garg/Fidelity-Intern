# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def dsp(self):
#         print(self.name, self.age)


# s = Student('Ravi', 20)
# s.dsp()


# classmethod

class Student:
    __a = 10

    def dsp(self):
        print(self.__a)

    @classmethod
    def m1(cls):
        print(cls.__a)


s = Student()
s.dsp()
