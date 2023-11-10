from bankaccount import *
from currentaccount import *
from savingaccount import *
from fixeddeposit import *
from random import *

def main():
    accounts = []
    accounts.append(CurrentAccount(randint(5000, 5000000)))
    accounts.append(SavingAccount(randint(5000, 5000000)))
    accounts.append(FixedDeposit(randint(5000, 5000000)))
    for i in range(20):
        account = accounts[randint(0, 2)]
        choice = randint(0, 5)
        if choice == 0: account.deposit(randint(100, 5000000))
        elif choice == 1: account.withdraw(randint(100, 5000000))
        elif choice == 2: account.debit(randint(100, 1000))
        elif choice == 3: account.credit(randint(100, 1000))
        elif choice == 4: account.terminate()
        else:
            account_type = account.get_account_type()
            if account_type == 'CURRENT':
                account.debit_bank_charges()
            elif account_type == 'SAVING':
                account.credit_daily_commision()
            else:
                account.credit_commission()
    for account in accounts:
        print(account)
    for account in accounts:
        account.print_account()

main()