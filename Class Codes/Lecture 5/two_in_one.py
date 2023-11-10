import random

def two_in_one():
    a = int(input("Enter Any Number Smaller than 16:"))
    b = int(input("Enter Any Number Smaller than 16:"))
    x = a
    x = x | (b<<4)
    print (x)

two_in_one()
