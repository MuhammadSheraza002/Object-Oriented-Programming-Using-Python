class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
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


    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
        beds=input("Enter number of bedrooms: "),
        baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


