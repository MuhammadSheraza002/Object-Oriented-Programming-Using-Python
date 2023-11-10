from datetime import *
from abc import ABC,abstractmethod

class BankAccount(ABC):
    total_accounts = 0
    def __init__(self,open_balance,account_type):
        BankAccount.total_accounts+=1
        self.open_balance = open_balance
        self.account_type = account_type
        dt = datetime.now()
        self.open_date = f'{dt.day}:{dt.month}:{dt.year}'
        self.account_no = BankAccount.total_accounts

    def Depodite(self,amount):
        self.open_balance += amount

    @abstractmethod
    def Withdraw(self,amount):
        if self.open_balance>=amount:
            self.open_balance -= amount
        else:
            print('Your balance is ',amount-self.open_balance,'rupees less')

    def Credit(self,amount):
        self.open_balance += amount

    def Debit(self, amount):
        self.open_balance -= amount

    def get_balance(self):
        return self.open_balance

    def get_account_type(self):
        return self.account_type

    def get_total_accounts(self):
        return BankAccount.total_accounts

    @abstractmethod
    def __str__(self):
        return f'{self.account_no}\t{self.account_type}\t{self.open_balance}'

