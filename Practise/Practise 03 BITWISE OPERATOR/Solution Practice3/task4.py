import random

def main():
    n = random.randint(0,255)
    print (f'Number: {n}')
    mask  = 1
    count_bit_1 = 0
    for i in range(8):  #We are working on 8 bits only
        if (n & mask) == 0:        #Bit is off
            n = (n | mask)
        else:                       #Bit is on
            n = (n & (255 - mask))
        mask *= 2
    print (f'After Flipping: {n}')


main()


