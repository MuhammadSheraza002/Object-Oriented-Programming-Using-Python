from transaction import *

class Cheque_Deposit(Transaction):
    def __init__(self, amount, cheque_no, bank, purpose='Transfer'):
        super().__init__('Ch_Wd', amount, CREDIT, 0) #Ch_Wd for cheque withdraw
        self.__cheque_no = cheque_no
        self.__purpose = purpose

    def __str__(self):
        return super().__str__() + f'{self.__cheque_no}\t{self.__purpose}\n'

    #Cash Deposit
    #Demand Draft
    #Pay Ordered
    #Utility Bill Payment

def main():
    t = Cheque_Deposit(10000, 'AB123','MCB')
    print(t)

main()