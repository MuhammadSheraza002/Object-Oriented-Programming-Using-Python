from datetime import *
from date import *
ACTIVE = True
TERMINATED = False
class BankAccount:
    total_accounts = 0
    def __init__(self, balance, account_type):
        BankAccount.total_accounts += 1
        self.__account_no = BankAccount.total_accounts
        self.__balance = balance
        self.__account_type = account_type
        dt = datetime.now()
        self.__openning_date = Date(dt.day, dt.month, dt.year)
        self.__status = ACTIVE
        print (f'Account no: {self.__account_no} of {self.__account_type} type is opened with balance: {self.__balance}')

    def deposit(self, amount):
        if self.__status == ACTIVE:
            self.__balance += amount
            print (f'{amount} is credited into Account no: {self.__account_no}')
        else:
            print ('This account is terminated')
    def withdraw(self, amount):
        if self.__status == ACTIVE:
            if self.__balance >= amount:
                self.__balance -= amount
                print (f'{amount} is debited into Account no: {self.__account_no}')
            else:
                print (f'Account no: {self.__account_no} is short of {amount-self.__balance} for withdraw')
        else:
            print ('This account is termid')
    def credit(self, amount):
        if self.__status == ACTIVE:
            self.__balance += amount
            print (f'{amount} is credited into Account no: {self.__account_no}')
        else:
            print ('This account is terminated')
    def debit(self, amount):
        if self.__status == ACTIVE:
            self.__balance -= amount
            print (f'{amount} is debited into Account no: {self.__account_no}')
        else:
            print ('This account is terminated')
    def get_balance(self):
        if self.__status == ACTIVE:
            return self.__balance
        else:
            print ('This account is terminated')
    def set_balance(self, balance):
        if self.__status == ACTIVE:
            self.__balance = balance
        else:
            print ('This account is terminated')
    def get_total_accounts(self):
        if self.__status == ACTIVE:
            return BankAccount.total_accounts
        else:
            print ('This account is terminated')
    def __str__(self):
        if self.__status == ACTIVE:
            return f'{self.__account_no}\t{self.__account_type}\t{self.__balance}'
        else:
            return f'{self.__account_no}\t{self.__status}'
    def print_account(self):
        print (f'Account No: {self.__account_no}')
        print (f'Opening Date: {self.__openning_date}')
        print (f'Type: {self.__account_type}')
        print (f'Balance: {self.__balance}')
        if self.__status == TERMINATED:
            print (f'This account is terminated')
    def terminate(self):
        self.__status = TERMINATED
    def get_status(self):
        return self.__status
    def get_account_type(self):
        return self.__account_type

