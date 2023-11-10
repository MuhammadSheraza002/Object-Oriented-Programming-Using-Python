from rental import *
from apartment import *

class ApartmentRental(Rental, Apartment):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Apartment.__init__(self, **kwargs)

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    #prompt_init = staticmethod(prompt_init)

    def __str__(self):
        s = Apartment.__str__(self)
        return s + '\n' + super().__str__()
