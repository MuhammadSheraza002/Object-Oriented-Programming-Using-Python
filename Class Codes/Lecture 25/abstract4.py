'''
When we use abstract class
We use abstract class when they are some common features shared by other
objects as they are
For example we have a parent class Park army it has three child classes,
 army air force and Navy
In three child classes army air force and Navy one parameter is common which
is gun and area is different in all three so here we will use abstract class
 and pak army will have a gun class which is concrete method and other is area which is different in army Air Force and Navy so it will be associated with abstract method
'''
from abc import ABC,abstractmethod

class Pak_Army(ABC):
    def gun(self):
        print('Gun')
    @abstractmethod
    def area(self):
        pass

class Army(Pak_Army):
    def area(self):
        print('Area=Land')

class AirForce(Pak_Army):
    def area(self):
        print('Area=Sky')

class Navy(Pak_Army):
    def area(self):
        print('Area=Sea')


def main():
    army = Army()
    army.gun()
    army.area()

    airforce = AirForce()
    airforce.gun()
    airforce.area()

    navy = Navy()
    navy.gun()
    navy.area()

main()
