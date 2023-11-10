from purchase import *
from apartment import *

class ApartmentPurchase(Purchase, Apartment):
    def __init__(self):
        price=input('What is the selling price? ')
        taxes=input('What are the estimated taxes? ')
        super().__init__(price, taxes)
        Apartment.__init__(self)
    def __str__(self):
        s = Apartment.__str__(self)
        return s + '\n' + super().__str__()
