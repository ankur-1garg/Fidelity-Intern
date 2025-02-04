# try:
#     y = int(input("Enter a number: "))
#     print(10/y)
# except ZeroDivisionError:
#     print("Zero Division Error")
# except ValueError:
#     print("Value Error")
# else:
#     print("No exception")
# finally:
#     print("Finally block")


# custom exception
class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg


age = int(input("Enter your age: "))
if age < 18:
    raise TooYoungException("You are too young to vote")
