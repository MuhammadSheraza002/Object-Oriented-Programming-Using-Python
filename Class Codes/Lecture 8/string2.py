def extract_number(s):
    n = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            n = n * 10 + int(s[i]) #n = n * 10 + int(ord(s[i])-ord('0'))
    return n

def strings2():
    s = input("Enter any string with only one number in between, no other digits: ")
    n =extract_number(s)
    print (f'Number: {n}')
    print (f'Number x 10: {n*10}')

strings2()



