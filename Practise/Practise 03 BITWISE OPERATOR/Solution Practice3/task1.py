import random

def main():
    n = random.randint(0,255)
    print (f'Number is: {n}')
    mask  = 1
    for i in range(8):  #We are working on 8 bits only
        if (n & mask) == 0:
            print (f'Bit {i+1} is off')
        else:
            print (f'Bit {i+1} is on')
        mask *= 2

main()
