from currentaccount import *

class OverdraftAccount(CurrentAccount):
    MINIMUM_BALANCE = -50000
    def __init__(self, balance):
        super().__init__(balance, 'OD')
    def debit_bank_charges(self):
        self.debit(500)
    def withdraw(self, amount):
        if self.get_status() == ACTIVE:
            balance = self.get_balance()
            if balance - amount >= OverdraftAccount.MINIMUM_BALANCE:
                self.set_balance(balance - amount)
                print (f'{amount} is debited into Account no: {self.get_account__no()}')
            else:
                print (f'Account no: {self.get_account_no()} is short of {amount + -self.get_balance()} for withdraw')
