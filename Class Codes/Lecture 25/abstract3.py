'''
                                Rules
1. we cannot create object of abstract method of abstract class.
 it must be in child class
2. if you are inheriting any abstract class you must provide a implementation
of a function or make this class abstract it means that if you are inheriting
any abstract class the class in which you are inherited inheriting
it must have a inherited abstract method function of parent class with the same
 signature(name)
'''

from abc import *

class My_ABC(ABC):
    @abstractmethod
    def abstract_function(self):
        print ('I am abstract function')


def main():
    my_abc = My_ABC()
    my_abc.abstract_function()

main()
