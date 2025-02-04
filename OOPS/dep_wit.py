class Customer:
    # Constructor to initialize name and balance
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Method to deposit amount
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # Method to withdraw amount
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance')  # Check for sufficient balance
            return self.balance
        else:
            self.balance -= amount
            return self.balance


C = Customer('Ravi', 1000)       # Creating Customer object
print(C.deposit(500))
print(C.withdraw(500))
