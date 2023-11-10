def one_bits():
    x = int(input("Enter number:"))
    count = 0
    for i in range(32):
        if ((x & (2 ** i))) != 0:
            print (f'Bit {i+1} is on')
one_bits()

