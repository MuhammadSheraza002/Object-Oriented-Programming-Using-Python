from rental import *
from house import *

class HouseRental(Rental, House):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        House.__init__(self, **kwargs)

    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    #prompt_init = staticmethod(prompt_init)

    def __str__(self):
        s = House.__str__(self)
        return s + '\n' + super().__str__()

