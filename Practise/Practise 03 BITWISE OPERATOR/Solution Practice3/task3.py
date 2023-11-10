import random

def main():
    t = random.randint(0,1)
    if t==0:
        n = 2 ** random.randint(2,7)
    else:
        n = random.randint(0,255)
    print (f'Number: {n}')
    mask  = 1
    count_bit_1 = 0
    for i in range(8):  #We are working on 8 bits only
        if (n & mask) != 0:        #Bit is on
            count_bit_1 += 1
        mask *= 2
    if count_bit_1 == 1:
        print(f'Number is in power of 2')
    else:
        print(f'Number is not in power of 2')

main()

