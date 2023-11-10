import random as r

def print_factors(n):
    print(f'Factors of {n} are: ', end='')
    d = 2
    while d <= n/2:
        if n % d == 0:
            n = int(n / d)
            print (d, end=' ')
            d = 2
        else:
            d += 1
    print(n)        #print remaining number, which is not divided yet

def task4():
    print_factors(r.randint(50,500))
    print_factors(r.randint(50,500))
    print_factors(r.randint(50,500))
    print_factors(3072)

task4()
