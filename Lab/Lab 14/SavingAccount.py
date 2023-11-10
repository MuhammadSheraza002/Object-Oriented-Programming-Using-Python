from BankAccount import *

class CurrentAccount(BankAccount):
    def __init__(self,open_balance,account_type='Saving'):
        super().__init__(open_balance,account_type)

    def credit_daily_commission(self):
        BankAccount.Credit(self,self.open_balance*.008)

    def Withdraw(self):
        BankAccount.Withdraw(self,100)

    def __str__(self):
        BankAccount.__str__(self)

