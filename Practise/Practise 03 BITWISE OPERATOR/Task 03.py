
def main():
    number = int(input('Enter number: '))
    i = 0
    while 2**i <=number:
        if 2**i == number:
            return True
        i+=1
    return False

print(main())