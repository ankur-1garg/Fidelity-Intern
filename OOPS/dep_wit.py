class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance')
            return self.balance
        else:
            self.balance -= amount
            return self.balance


C = Customer('Ravi', 1000)
print(C.deposit(500))
print(C.withdraw(2000))
print(C.withdraw(500))
