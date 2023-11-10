from purchase import *
from house import *
class HousePurchase(Purchase, House):
    def __init__(self):
        price=input('What is the selling price? ')
        taxes=input('What are the estimated taxes? ')
        super().__init__(price, taxes)
        House.__init__(self)
    def __str__(self):
        s = House.__str__(self)
        return s + '\n' + super().__str__()
