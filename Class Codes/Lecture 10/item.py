#define class to represent Item, where each item has three members. First member is code (string value like A24).
#Second data member is price and third data member is quantity. Keep data
# members private. Write following member functions:
#initializer function to initialize data member with 3 parameters provided
# in the function
#3 setter functions, for each data member write separate set function
#write 3 getter functions, to get value of data members
#write show function, to show value of three data members in a single line
#write compare function, compare function will return 1 if price of first item is greater than price of second
#iterm, return -1 if price of first item is smaller than price of second item, otherwise return zero
class Item:
    def __init__(self, code, price, quantity):
        self.__code = code        #data members are private, being started with __
        self.__price = price
        self.__quantity = quantity

    def set_code(self, code):
        self.__code = code        #data members are private, being started with __

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_code(self):
        return self.__code
        return self.__code

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def show(self):
        print (f'Code: {self.__code}, Price: {self.__price}, Quantity: {self.__quantity}')

    def compare(self, item):
        if self.__price > item.__price:
            return 1
        elif self.__price < item.__price:
            return -1
        return 0
