import random

def generate_random_array(x, size):
    for i in range(size):
        x.append(random.randint(0, 50))

def copy(x, y):
    for i in range(len(x)):
        y.append(x[i])

def linear_search(x, element):
    for i in range(len(x)):
        if x[i] == element:
            return True
    return False

def binary_search(x, element):
    start = 0
    end = len(x) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if x[middle] == element:
            return True
        elif x[middle] > element:
            end = middle - 1
        else:
            start = middle + 1
    return False

def main():
    x=[]
    generate_random_array(x, 20)
    print(x)
    y = []
    copy(x, y)
    y.sort()
    print (y)
    for i in range(20):
        temp = random.randint(0, 50)
        if linear_search(x, temp) == True:
            print (f'{temp} found by linear search')
        else:
            print (f'{temp} not found by linear search')
        if binary_search(y, temp) == True:
            print (f'{temp} found by binary search')
        else:
            print (f'{temp} not found by binary search')


main()
