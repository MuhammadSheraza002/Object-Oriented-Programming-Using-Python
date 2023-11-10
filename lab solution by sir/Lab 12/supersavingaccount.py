from savingaccount import *

class SuperSavingAccount(SavingAccount):
    MINIMUM_BALANCE = 50000
    def __init__(self, balance):
        super().__init__(balance, 'S_SAVING')
    def withdraw(self, amount):
        if self.get_status() == ACTIVE:
            balance = super().get_balance()
            if balance >= amount + SuperSavingAccount.MINIMUM_BALANCE:
                super().set_balance (balance - amount)
                print (f'{amount} is debited into Account no: {self.__account_no}')
            else:
                print (f'Account no: {self.__account_no} is short of {amount-self.__balance} for withdraw')
        else:
            print ('This account is termid')
    def print_account(self):
        super().print_account()
        print (f'Minimum Balance Required: {SuperSavingAccount.MINIMUM_BALANCE}')
    def credit_daily_commision(self):
        commission = self.get_balance() * 0.01
        self.credit(commission)