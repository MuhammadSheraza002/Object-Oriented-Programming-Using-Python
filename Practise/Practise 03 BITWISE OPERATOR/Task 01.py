number = int(input('Enter number: '))
i = 0
while 2**i <= number:
    if (number) & (2 ** i) == (2 ** i):
        print(f"Bit {i+1} is on")
    i+=1

