class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)

account = BankAccount()

account.deposit(500)
account.withdraw(300)
account.show_balance()