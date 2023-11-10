from Transaction import *
class CashWithdraw(Transaction):
    def __init__(self,amount,cheque_no):
        super().__init__(amount,'Withdraw')
        self.cheque_no = cheque_no

    def __str__(self):
        super().__str__()


