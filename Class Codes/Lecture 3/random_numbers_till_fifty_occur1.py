import random
def random_numbers_till_fifty_occur1():
    while True:
        n = random.randint(0,100)
        print (n, end=" ")
        if n == 50:
            break

random_numbers_till_fifty_occur1()
