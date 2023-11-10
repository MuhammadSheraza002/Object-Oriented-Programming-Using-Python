from property import *
from functions import *

class House(Property):
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')
    def __init__(self, num_stories=1, garage='YES', fenced='YES'):
        super().__init__()
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories
    def __str__(self):
        s = super().__str__()
        s += 'HOUSE DETAILS\n'
        s += '# of stories: {}'.format(self.num_stories)
        s += '\ngarage: {}'.format(self.garage)
        s += '\nfenced yard: {}'.format(self.fenced)
        return s
    def set_values(self):
        self.fenced = get_valid_input('Is the yard fenced? ',House.valid_fenced)
        self.garage = get_valid_input('Is there a garage? ',House.valid_garage)
        self.num_stories = input('How many stories? ')


