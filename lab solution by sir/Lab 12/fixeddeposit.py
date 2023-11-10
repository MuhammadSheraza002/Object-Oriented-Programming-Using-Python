from bankaccount import *

class FixedDeposit(BankAccount):
    def __init__(self, balance):
        super().__init__(balance,'FIXED')
    def credit_commission(self):
        commission = self.get_balance() * 0.12
        self.credit(commission)
    def withdraw(self, amount):
        print ('This is a fixed deposit account, widthdrawal not allowed')