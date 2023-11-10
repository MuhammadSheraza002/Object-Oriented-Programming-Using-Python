import random

def check_random_number_sum():
    a = random.randint(10, 50)
    b = random.randint(10, 50)
    print ("A: ", a)
    print ("B: ", b)
    answer = int(input("Sum: "))
    if answer == a+b:
        print ("Your answer is correct")
    else:
        print ("Sorry, correct answer is ", a+b)

check_random_number_sum()
