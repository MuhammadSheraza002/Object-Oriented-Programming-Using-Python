from functions import *
from apartment_purchase import *
from apartment_rental import *
from house_purchase import *
from house_rental import *
class Agent:
    class_dict = {('house', 'rental'): HouseRental, ('house', 'purchase'): HousePurchase, ('apartment', 'rental'): ApartmentRental,('apartment', 'purchase'): ApartmentPurchase }
    def __init__(self):
        self.property_list = []

    def add_property(self):
        property_type = get_valid_input('What type of property? ', ('house', 'apartment')).lower()
        payment_type = get_valid_input( 'What payment type? ', ('purchase', 'rental')).lower()
        item = None
        if property_type == 'house' and payment_type == 'purchase': item = HousePurchase()
        elif property_type == 'house' and payment_type == 'rental': item = HouseRental()
        if property_type == 'apartment' and payment_type == 'purchase': item = ApartmentPurchase()
        elif property_type == 'apartment' and payment_type == 'rental': item = ApartmentRental()
        self.property_list.append(item)

    def show_all_properties(self):
        for property in self.property_list:
            print(property)

    def show_match_property(self):
        property_type = get_valid_input('What type of property? ', ('house', 'apartment')).lower()
        payment_type = get_valid_input( 'What payment type? ', ('purchase', 'rental')).lower()
        for property in self.property_list:
            if type(property) == Agent.class_dict[(property_type, payment_type)]:
                print(property)
    def modify_property(self):
        property_no = int(input ('Enter property no to modify: '))
        if property_no < 1 or property_no > len(self.property_list):
            print ('Invalid Input')
        else:
            self.property_list[property_no-1].set_values()



