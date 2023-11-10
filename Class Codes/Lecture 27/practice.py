from apartment_rental import *
from apartment_purchase import *
from apartment_rental import *
from house_rental import *
from house_purchase import *

property_type= input ("What type of property?")
payment_type= input ( "What payment type?")
ObjectClass= self.type_map[( property_type , payment_type)]
self.type_map = {('house', 'rental'):HouseRental,
                ('house', 'purchase'):HousePurchase,
                ('apartment', 'rental'):ApartmentRental,
                ('apartment', 'purchase'):ApartmentPurchase
                    }
