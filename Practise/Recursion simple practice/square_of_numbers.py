def square_of_numbers(n,i=0,sum=0):
    if i == n:
        return sum + i ** 2
    return sum + square_of_numbers(n,i=i+1,sum=+i**2)

from random import randint

n = randint(1,10)
print(n)
print(square_of_numbers(n))

