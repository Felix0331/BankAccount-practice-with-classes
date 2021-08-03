class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficent funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        x = self.balance
        print(f'Balance: ${x}')
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance*self.int_rate
        return self

account1 = BankAccount(.10, 100)
account2 = BankAccount(.10, 200)

account1.deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()