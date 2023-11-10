class Student:
    def __init__(self, roll_no):
        self.__roll_no = roll_no
        self.__mid = 0
        self.__sessional = 0
        self.__final = 0

    def set_mid(self, mid):
        self.__mid = mid
    def set_final(self, final):
        self.__final = final
    def set_sessional(self, sessional):
        self.__sessional = sessional

    def get_midterm(self):
        return self.__mid
    def get_final(self):
        return self.__final
    def get_sessional(self):
        return self.__sessional

    def __str__(self):
        return f'{self.__roll_no}\t{self.__mid}\t{self.__sessional}\t{self.__final}'


