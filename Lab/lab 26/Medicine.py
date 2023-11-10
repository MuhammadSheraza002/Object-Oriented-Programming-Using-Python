class medicine:
    count=0
    def __init__(self,name,potency='',quantity=10,retail_price=1,sale_price=1):
        medicine.count+=1
        self.__sr_no = medicine.count
        self.__potency = potency
        self.__name = name
        self.set_quantity(quantity)
        self.set_retail_price(retail_price)
        self.set_sale_price(sale_price)

    def set_quantity(self,quantity):
        self.__quantity = quantity

    def set_retail_price(self,retail_price=1):
        if retail_price<=0:
            retail_price = 1
        self.__retail_price = retail_price

    def set_sale_price(self,sale_price=1):
        if sale_price < self.__retail_price:
            sale_price = 0.2 * self.__retail_price + self.__retail_price
        self.__sale_price = sale_price

    def get_quantity(self,quantity):
        return self.__quantity

    def get_retail_price(self,retail_price):
        return self.__retail_price

    def get_sale_price(self,sale_price):
        return self.__sale_price

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def about():
        print('medicine class')

    def __str__(self):
        retur f''