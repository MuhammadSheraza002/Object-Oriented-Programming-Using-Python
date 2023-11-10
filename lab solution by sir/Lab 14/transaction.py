from abc import *
from datetime import *

DEBIT = True
CREDIT = False

class Transaction(ABC):
    def __init__(self, transaction_type, amount, debit_credit=DEBIT, charges=0):
        self.__date_time = datetime.now()
        self.transaction_type = transaction_type
        self.__amount = amount
        self.__debit_credit = debit_credit
        self.__charges = charges

    @abstractmethod
    def __str__(self):
        output_string = f'{self.__date_time}\t{self.transaction_type}\t{self.__amount}\t{self.__charges}\t'
        if self.__debit_credit == DEBIT:    output_string += 'Debit\t'
        else:   output_string += 'Credit\t'
        return output_string

    #Electronic Fund Transfer
    #Cheque Deposit
    #Cheque Credit
    #Demand Draft
    #Pay Ordered
    #Utility Bill Payment