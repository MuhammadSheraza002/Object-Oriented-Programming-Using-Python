from bankaccount import *

class SavingAccount(BankAccount):
    def __init__(self, balance, account_type='SAVING'):
        super().__init__(balance, account_type)
    def credit_daily_commision(self):
        commission = self.get_balance() * 0.008
        self.credit(commission)