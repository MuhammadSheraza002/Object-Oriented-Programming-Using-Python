from bankaccount import *
from currentaccount import *
from savingaccount import *
from fixeddeposit import *
from supersavingaccount import *
from overdraft import *
from transaction import *
from cash_deposit import *
from cash_withdrawal import *
from cheque_deposit import *
from check_withdrawal import *

accounts=[]
accounts.append(CurrentAccount(40000))
accounts.append(SavingAccount(90000))
accounts.append(SuperSavingAccount(240000))
accounts.append(OverdraftAccount(140000))
for account in accounts:
    print (account)

transactions=[]
transactions.append(Cash_Deposit(5000))
transactions.append(Cheque_Deposit(15000,'AA0102', 'HBL'))
transactions.append(Cash_Withdrawal(3000,'AB2103', 'UBL'))
#...
for transaction in transactions:
    print(transaction)