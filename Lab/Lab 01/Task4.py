import random

def print_series_between_random_numbers():
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    if a < b:
        for i in range(a, b+1):
            print (i,end=" ")
    else:
        for i in range(b, a+1):
            print (i,end=" ")

print_series_between_random_numbers()
