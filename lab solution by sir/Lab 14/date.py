class Date:
    def __init__(self, dd, month, year):
        self.__dd = dd
        self.__month = month
        self.__year = year

    def __str__(self):
        return f'{self.__dd}:{self.__month}:{self.__year}'