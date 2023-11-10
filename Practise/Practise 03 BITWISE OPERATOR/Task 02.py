number1 = int(input('Enter number: '))
number2 = int(input('Enter number: '))
i = 0
count=0
while 2**i <=number1 or 2**i <=number2 :
    if (number1) & (2 ** i) != (number2) & (2 ** i):
        count+=1
    i+=1
print('In %d and %d, %d bits are different'%(number1,number2,count))

