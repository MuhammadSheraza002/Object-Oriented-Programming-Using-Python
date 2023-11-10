from BankAccount import *

class CurrentAccount(BankAccount):
    def __init__(self,open_balance,account_type='Current'):
        super().__init__(open_balance,account_type)

    def debit_bank_charges(self):
        BankAccount.Debit(self,100)

    def Withdraw(self):
        BankAccount.Withdraw(self,100)

    def __str__(self):
        BankAccount.__str__(self)

