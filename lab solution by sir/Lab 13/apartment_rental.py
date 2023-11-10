from rental import *
from apartment import *

class ApartmentRental(Rental, Apartment):
    def __init__(self):
        super().__init__()
        Apartment.__init__(self)
    def __str__(self):
        s = Apartment.__str__(self)
        return s + '\n' + super().__str__()
