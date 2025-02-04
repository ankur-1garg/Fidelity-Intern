class P:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print("Parent class instance method")

    @classmethod
    def m2(cls):
        print("Parent class class method")

    @staticmethod
    def m3():
        print("Parent class static method")


class C(P):
    pass


c = C()
print(c.a)
