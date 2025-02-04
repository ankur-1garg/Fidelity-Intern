# Defining a class named Student
class Student:
    # Private class variable (name mangling will occur because of double underscores)
    __a = 10

    # Instance method to display the value of the private variable __a
    def dsp(self):
        # Accessing the private class variable using self
        print(self.__a)

    # Class method that can access class-level variables
    @classmethod
    def m1(cls):
        # Accessing the private class variable using cls
        print(cls.__a)


# Creating an instance of the Student class
s = Student()

# Calling the instance method dsp() using the object 's'
# This will print 10 because the instance method can access the private variable
s.dsp()

# Uncommenting the line below would call the class method without creating an object
# Student.m1()  # This will also print 10 because class methods can access class variables
# ##############################################################################################################
