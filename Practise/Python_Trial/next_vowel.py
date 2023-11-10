def print_next_vowel(c):
    if c<'E':
        print('E')
    elif c<'I':
        print('I')
    elif c<'O':
        print('O')
    elif c<'U':
        print('U')
    else:
        print('A')
    
def main():
    c = input()
    print_next_vowel(c)
    
main()
