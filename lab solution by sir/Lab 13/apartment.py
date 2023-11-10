from property import *
from functions import *

class Apartment(Property):
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')
    def __init__(self, balcony='YES', laundry='YES'):
        super().__init__()
        self.balcony = balcony
        self.laundry = laundry
    def __str__(self):
        s = super().__str__()
        s += 'APARTMENT DETAILS\n'
        s += f'laundry: {self.laundry}\n'
        s += f'has balcony: {self.balcony}\n'
        return s
    def set_values(self):
        self.laundry = get_valid_input('What laundry facilities does ' 'the property have? ', Apartment.valid_laundries)
        self.balcony = get_valid_input('Does the property have a balcony? ', Apartment.valid_balconies)
