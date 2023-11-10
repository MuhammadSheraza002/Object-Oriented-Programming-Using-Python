number1 = int(input('Enter number: '))
number2 = int(input('Enter number: '))
i = 1
count=0
while i <= 8:
    if (number1) & (2 ** (i - 1)) != (number2) & (2 ** (i - 1)):
        return False
    i += 1
return True


