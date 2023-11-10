import random
def print_prime_or_not2():
    n = random.randint(2,100)
    if n == 2:
        print (f'{n} is prime')
        return
    is_prime = True
    #we have checked by 0, if n is not divisible by 2, it will be divisible by any other even number
    if n % 2 == 0:
        print (f'{n} is not prime')
        return
    # no more check with even number required, so we will check for odd numbers only
    for i in range(3, n, 2):
        if n % i == 0:
            is_prime = False
            # to discontinue the loop because no more checking required, this step will improve time efficiency of program
            break 
    if is_prime:
        print (f'{n} is prime')
    else:
        print (f'{n} is not prime')

print_prime_or_not2()
