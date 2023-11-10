import random

def print_random_count_less_than_fifty():
    count_less_than_fifty = 0
    for i in range(1, 11):
        x = random.randint(0, 100)
        print (x, end=" ")
        if x < 50:
            count_less_than_fifty += 1
    print ()
    print (count_less_than_fifty, " numbers are less than fifty")
print_random_count_less_than_fifty()
