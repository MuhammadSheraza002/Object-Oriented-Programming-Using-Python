import random

def main():
    n1 = random.randint(0,16)
    n2 = random.randint(0,16)
    print (f'First Number: {n1}')
    print (f'Second Number: {n2}')
    mask  = 1
    different_bit_count = 0
    for i in range(4):  #Check only four bits
        if (n1 & mask) != (n2 & mask):
            different_bit_count = 1
            print(f'{n1} and {n2} are not equal')
            break
        mask *= 2
    if different_bit_count == 0:
        print(f'{n1} and {n2} are equal')

main()
