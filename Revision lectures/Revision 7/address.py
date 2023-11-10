class Address:
    def __init__(self, hn, bn, tn, cty, ctry):
        self.__house_no = hn
        self.__block_no = bn
        self.__town = tn
        self.__city = cty
        self.__country = ctry

    def __str__(self):
        return f'House #: {self.__house_no}\nBlock #: {self.__block_no}\nTown: {self.__town}\nCity: {self.__city}\nCountry: {self.__country}'

    def get_str(self):
        return f'{self.__house_no}\t{self.__block_no}\t{self.__town}\t{self.__city}\t  {self.__country}'
