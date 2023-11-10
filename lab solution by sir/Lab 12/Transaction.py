from datetime import *
from abc import ABC,abstractmethod

class Transaction(ABC):
    total_transactions = 0
    def __init__(self, amount, transaction_type):
        Transaction.total_transactions +=1
        self.transaction_no = Transaction.total_transactions
        self.amount = amount
        self.transaction_type = transaction_type
        dt = datetime.now()
        self.transaction_date = f'{dt.day}:{dt.month}:{dt.year}'

    def Depodite(self,amount):
        self.open_balance += amount

    @abstractmethod
    def Withdraw(self,amount):
        if self.open_balance>=amount:
            self.open_balance -= amount
        else:
            print('Your balance is ',amount-self.open_balance,'rupees less')

    @abstractmethod
    def Credit(self,amount):
        self.amount += amount

    @abstractmethod
    def Debit(self, amount):
        self.amount -= amount



    @abstractmethod
    def __str__(self):
        return f'{self.transaction_no}\t{self.transaction_date}\t{self.amount}\t{self.transaction_type}'