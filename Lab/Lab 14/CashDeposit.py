from Transaction import *
class CashDeposit(Transaction):
    def __init__(self,amount):
        super().__init__(amount,'Cash Deposit')

    def __str__(self):
        super().__str__()
