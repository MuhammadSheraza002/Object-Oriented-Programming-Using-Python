from functions import *
from apartment_purchase import *
from apartment_rental import *
from house_purchase import *
from house_rental import *
class Agent:
    def __init__(self):
        self.property_list = []
        self.type_map = {('house', 'rental'): HouseRental, ('house', 'purchase'): HousePurchase, ('apartment', 'rental'): ApartmentRental,('apartment', 'purchase'): ApartmentPurchase }
    def add_property(self):
        property_type = get_valid_input("What type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input( "What payment type? ", ("purchase", "rental")).lower()
        ObjectClass = self.type_map[(property_type, payment_type)]
        init_args = ObjectClass.prompt_init()
        self.property_list.append(ObjectClass(**init_args))

    def show_all_properties(self):
        for property in self.property_list:
            print(property)

    def show_match_property(self):
        property_type = get_valid_input('What type of property? ', ('house', 'apartment')).lower()
        payment_type = get_valid_input( 'What payment type? ', ('purchase', 'rental')).lower()
        for property in self.property_list:
            if type(property) == self.type_map[(property_type, payment_type)]:
                print(property)

    def modify_property(self):
        property_no = int(input ('Enter property no to modify: '))
        if property_no < 1 or property_no > len(self.property_list):
            print ('Invalid Input')
        else:
            self.property_list[property_no-1].set_values()



