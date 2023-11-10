from negative_number_exception import *

def enterage(age):
    if age < 0:
        raise NegativeNumberException('Only positive integers are allowed')
    if age % 2 == 0:
        print('Age is Even')
    else:
        print('Age is Odd')

try:
    num = int(input('Enter your age: '))
    enterage(num)
except NegativeNumberException as nne:  #Here nne is object of NegativeNumberException
    print(nne)                          #str of NegativeNumberException is called
except:
    print('Something is wrong')
