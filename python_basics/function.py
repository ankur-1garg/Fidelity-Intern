# Importing a custom module named fidelity_ds and aliasing it as fil2
import fidelity_ds as fil2
# Importing another custom module named fidelity_prg and aliasing it as fil
import fidelity_prg as fil

# Prompting the user to enter a month
# Takes input from the user to specify the month
month = input("Enter the month: ")

# Calling the days_in_month function from the fidelity_ds module with the user's input
# Prints the number of days in the entered month
print(fil2.days_in_month(month))

# The following are previously written code snippets showcasing various Python concepts:

# Function accepting variable number of arguments
# def func(*a):
#     return a  # Returns all passed arguments as a tuple

# s = func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(type(s))  # Prints the type of 's', which will be a tuple

# Function accepting keyword arguments
# def fun(**kwargs):
#     for k, val in kwargs.items():
#         return (k, val)  # Returns the first key-value pair as a tuple

# s = fun(a=1, b=2, c=3)
# print(type(s))  # Prints the type of 's', which will be a tuple

# Creating a tuple with a single element
# t1 = (2,)
# print(type(t1))  # Ensures it's recognized as a tuple using a trailing comma

# Assigning a function to a variable
# def func(a, b):
#     return a + b  # Returns the sum of a and b

# p = func
# print(p(2, 3))  # Calls the function using the new variable name

# Closure function example
# def f1(a):  # Outer function
#     def f2():  # Inner function
#         print(a)  # Accesses 'a' from the outer function's scope
#     return f2

# f1(2)()  # Calls the inner function returned by f1

# Demonstrating the use of the global keyword
# a = 10
# def func():
#     global a  # Declares 'a' as a global variable
#     a = a + 10  # Modifies the global 'a'
#     return a

# print(func())  # Prints the updated value of 'a'

# Generator function example
# def fun():
#     yield 'a'
#     yield 'b'
#     yield 'c'

# p = fun()
# print(next(p))  # Outputs 'a'
# print(next(p))  # Outputs 'b'

# Memory comparison between list and generator
# import sys
# l1 = [i for i in range(1000)]  # List comprehension
# g = (i for i in range(1000))  # Generator expression
# print(sys.getsizeof(l1))  # Memory size of the list
# print(sys.getsizeof(g))  # Memory size of the generator
# print(type(g))  # Confirms 'g' is a generator

# Function returning another function
# def outer(a):
#     def inner(b):
#         return a + b  # Adds 'a' from the outer function to 'b' from the inner function
#     return inner

# print(outer(10)(20))  # Calls the returned inner function immediately

# Demonstrating function as an argument
# def f1(a, b):
#     print(a + b)

# def f2(fun):
#     print("hello")

# f2(f1(10, 20))  # Calls f1 first, then passes its result to f2

# Decorator function example


def decorator(fun):
    def wrapper(a, b):
        print("hello")  # Prints before the function call
        print(fun(a, b))  # Calls the original function
        print("end")  # Prints after the function call
    return wrapper


@decorator  # Applying the decorator to the function
def print_message(a, b):
    return a + b  # Returns the sum of a and b


print_message(10, 20)  # Calls the decorated function
