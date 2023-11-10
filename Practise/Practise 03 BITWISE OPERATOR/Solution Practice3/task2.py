import random

def main():
    n1 = random.randint(0,255)
    n2 = random.randint(0,255)
    print (f'First Number: {n1}')
    print (f'Second Number: {n2}')
    mask  = 1
    different_bit_count = 0
    for i in range(8):  #We are working on 8 bits only
        if (n1 & mask) != (n2 & mask):
            different_bit_count += 1
        mask *= 2
    print(f'In {n1} and {n2}, {different_bit_count} bits are different')

main()

