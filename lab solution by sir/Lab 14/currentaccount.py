from bankaccount import *

class CurrentAccount(BankAccount):
    def __init__(self, balance, account_type='CURRENT'):
        super().__init__(balance, account_type)
    def debit_bank_charges(self):
        self.debit(100)
