'''def print_alphabet(n):
    for i in range(n):
        print(chr(i+65),end='')
    print()
    for i in range(n):
        print(chr(i+97),end='')
    print()

def main():
    n = int(input())
    print_alphabet(n)

main()
'''

def alphabetic_loop(number):
    for index in range(ord('A'),ord('A')+number):
        print(chr(index),end='')
    print()
    for index in range(ord('a'),ord('a')+number):
        print(chr(index),end='')

def main():
    number = int(input("Enter positive integer: "))
    alphabetic_loop(number)

main()