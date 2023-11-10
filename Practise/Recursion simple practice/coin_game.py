def dec_bin(number):
    if number // 2 == 1:
        print(1)
        return
    print(number%2)
    dec_bin(number//2)

from random import randint
def main():
    n = randint(1,10)
    print(n)
    dec_bin(n)

main()


