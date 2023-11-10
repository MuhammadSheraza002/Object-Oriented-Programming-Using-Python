import random

def main():
    print('*** Enter Numbers to Print Cube, to Stop, Press -1 ***')
    while True:
        n = int(input('Number: '))
        if n == -1:
            break
        print (f'Cube: {n*n*n}')


main()
