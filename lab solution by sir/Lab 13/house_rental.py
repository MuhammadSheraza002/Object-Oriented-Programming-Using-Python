from rental import *
from house import *

class HouseRental(Rental, House):
    def __init__(self):
        super().__init__()
        House.__init__(self)
    def __str__(self):
        s = House.__str__(self)
        return s + '\n' + super().__str__()

