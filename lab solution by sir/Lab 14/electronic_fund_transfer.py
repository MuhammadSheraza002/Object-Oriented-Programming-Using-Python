from transaction import *

class Electronic_Fund_Transfer(Transaction):
    def __init__(self, amount, account_ref, charges = 100, debit_credit=DEBIT):
        super().__init__('E_F_T', amount, debit_credit, charges) #EFT for electronic fund transfer

        self.__account_ref = account_ref

    def __str__(self):
        return super().__str__() + f'{self.__account_ref}\n'

def main():
    t = Electronic_Fund_Transfer(10000, 'AB123', 20)
    print(t)

main()