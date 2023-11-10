from property import *
from functions import *

class Apartment(Property):
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')
    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
    def set_values(self):
        self.laundry = get_valid_input('What laundry facilities does ' 'the property have? ', Apartment.valid_laundries)
        self.balcony = get_valid_input('Does the property have a balcony? ', Apartment.valid_balconies)
    def __str__(self):
        s = super().__str__()
        s += 'APARTMENT DETAILS\n'
        s += f'laundry: {self.laundry}\n'
        s += f'has balcony: {self.balcony}\n'
        return s
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = ''
        balcony = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does " "the property have? ({})".format( ", ".join(Apartment.valid_laundries)))
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? " "({})".format(", ".join(Apartment.valid_balconies)))
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    prompt_init = staticmethod(prompt_init)
