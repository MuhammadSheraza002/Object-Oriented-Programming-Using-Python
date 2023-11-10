import random
def print_prime_or_not1():
    n = random.randint(2,100)
    if n == 2:
        print (f'{n} is prime')
        return
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            # to discontinue the loop because no more checking required, this step will improve time efficiency of program
            break 
    if is_prime:
        print (f'{n} is prime')
    else:
        print (f'{n} is not prime')

print_prime_or_not1()
