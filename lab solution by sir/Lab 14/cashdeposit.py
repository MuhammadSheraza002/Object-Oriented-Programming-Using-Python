from transaction import *

class Cash_Deposit(Transaction):
    def __init__(self, amount, purpose='Transfer'):
        super().__init__('C_Wd', amount, 'CREDIT', 0) #C_Wd for cash withdraw
        self.__purpose = purpose

    def __str__(self):
        return super().__str__() + f'\t{self.__purpose}\n'

