class BankAccount:
    account_instances = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_instances.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) > 0:
            self.balance -= amount
        else:
            print(f'Not enough funds.\nYour account currently holds {self.balance}. Thank you')
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance* self.int_rate)
        else:
            print('Your Account is currently Negative.')
        return self
ryan = BankAccount(.5,300)
justin = BankAccount(.8,200)

ryan.deposit(100).deposit(200).deposit(300).withdraw(200).yield_interest().display_account_info()
justin.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()