try:
    y = int(input("Enter a number: "))
    print(10/y)
except ZeroDivisionError:
    print("Zero Division Error")
except ValueError:
    print("Value Error")
