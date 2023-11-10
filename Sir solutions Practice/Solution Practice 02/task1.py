import random

def main():
    sum = 0
    for i in range(5):
        #instead of input, I am taking random values, hope you can write n = int(input("Enter Value:"))
        n = random.randint(10,99)
        print (n, end=' ')
        sum += n
    print (f'\nSum: {sum}')
    print (f'Average: {sum/5}')

main()

