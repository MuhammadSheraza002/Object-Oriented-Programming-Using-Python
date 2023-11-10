class Property:
    def __init__(self, square_feet=100, beds=1, baths=1):
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    def __str__(self):
        s = 'PROPERTY DETAILS\n================\n'
        s += 'square footage: {}'.format(self.square_feet)
        s += '\nbedrooms: {}'.format(self.num_bedrooms)
        s += '\nbathrooms: {}'.format(self.num_baths)
        return s+'\n'

    def set_values(self):
        self.square_feet=input('Enter the square feet: ')
        self.beds=input('Enter number of bedrooms: ')
        self.baths=input('Enter number of baths: ')
