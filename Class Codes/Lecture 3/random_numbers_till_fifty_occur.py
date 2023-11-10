import random
def random_numbers_till_fifty_occur():
    n = 0
    while n != 50:
        n = random.randint(0,100)
        print (n, end=" ")

random_numbers_till_fifty_occur()
