from Transaction import *
class ChequeWithdraw(Transaction):
    def __init__(self,amount,chequeno,title,bank):
        super().__init__(amount,'Withdrawal')
        self.cheque_no = chequeno
        self.title = title
        self.bank = bank

    def __str__(self):
        super().__str__() + f'{self.cheque_no}\t{self.title}\t{self.bank}'


