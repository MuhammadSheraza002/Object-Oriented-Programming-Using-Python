import random

def main():
    n = random.randint(3,10)
    print(f'Number of terms : {n}') #again I am taking random value, instead of input
    for i in range(1, n+1):
        print (f'Number is : {i} and cube of the {i} is :{i*i*i}')

main()

