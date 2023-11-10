from transaction import *

class Cash_Deposit(Transaction):
    def __init__(self, amount, purpose='Transfer'):
        super().__init__('Ch_Wd', amount, CREDIT, 0) #Ch_Wd for cheque withdraw
        self.__purpose = purpose

    def __str__(self):
        return super().__str__() + f'\t{self.__purpose}\n'
