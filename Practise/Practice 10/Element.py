from datetime import datetime
from random import randint

def main():
    e1 = Element(50)
    e1.set(50)
    print(e1)
    e2 = Element(30)
    print(e2)
    e1.now()
    print(e1)
    print(e1==e2)
    print(e1>e2)
    print(e1<e2)
    print(e1.is_older(e2))
    print(e1.is_same_time(e2))
    print(e1.greater_count(e2))
    print(e1.increment_by(50))
class Element:

    def __init__(self,value):
        self.__value = value
        self.now()
        self.__count+=1

    def __str__(self):
        return f'{self.__value}-{self.__hour}:{self.__minute}:{self.__second} ({self.__count})'

    def now(self):
        time = datetime.now()
        self.__hour = time.hour
        self.__minute = time.minute
        self.__second = time.second
        self.__count = 0

    def set(self,value):
        self.__value = value
        time = datetime.now()
        self.__hour = time.hour
        self.__minute = time.minute
        self.__second = time.second
        count = 0

    def get_value(self):
        return self.__value

    def get_count(self):
        return self.__count

    def get_time(self):
        return f'{self.__hour}:{self.__minute}:{self.__second}'

    def __eq__(self, other):
        return self.__value==other.__value

    def __gt__(self, other):
        return self.__value > other.__value

    def __lt__(self, other):
        return self.__value < other.__value

    def increment_by(self,n):
        return n+self.__value

    def is_older(self,other):
        return self.__hour< other.__hour and self.__minute < other.__minute and self.__second < other.__second

    def is_same_time(self,other):
        return self.__hour == other.__hour and self.__minute == other.__minute and self.__second == other.__second

    def greater_count(self,other):
        return self.__count>other.__count

main()