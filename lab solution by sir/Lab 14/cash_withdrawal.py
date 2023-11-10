from transaction import *

class Cash_Withdrawal(Transaction):
    def __init__(self, amount, cheque_no, purpose, debit_credit=DEBIT, charges=0):
        super().__init__('Ch_Dp', amount, debit_credit, charges) #Ch_Dp for cheque deposit
        self.__cheque_no = cheque_no
        self.__purpose = purpose

    def __str__(self):
        return super().__str__() + f'{self.__cheque_no}\t{self.__purpose}\n'