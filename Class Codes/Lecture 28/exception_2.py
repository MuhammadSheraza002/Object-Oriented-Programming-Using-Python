try:
    number = int(input('Enter number 1-10: '))
    print('You have entered number: ',number)
except(ValueError):
    print('Error..numbers only')
