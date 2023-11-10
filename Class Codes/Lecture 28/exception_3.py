def enterAge(age):
    if age<0:
        raise ValueError('Only positive integers are allowed')
    if age % 2 ==0:
        print('Entered Age is even')
    else:
        print('Entered Age is odd')

try:
    num = int(input('Enter your age: '))
    enterAge(num)
except ValueError:
    print('Only positive integers are allowed')
