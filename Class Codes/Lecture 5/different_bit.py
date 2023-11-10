def different_bit():
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    count = 0
    for i in range(32):
        if ((x & (2 ** i))) != ((y & (2 ** i))):
            count += 1
    print (f'In {x} and {y}, {count} bits are different')
different_bit()# Write your code here :-)
