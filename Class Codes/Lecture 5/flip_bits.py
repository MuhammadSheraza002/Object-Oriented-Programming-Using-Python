def flip_bits():
    x = int(input("Enter number:"))
    count = 0
    for i in range(8):
        if ((x & (2 ** i))) == 0:
            x = x | (2 ** i)        #On ith bit, because it is off
        else:
            x = x & (255 - 2 ** i)  #Off ith bit, because it is on
    print (f'After flipping: {x}')
flip_bits()
