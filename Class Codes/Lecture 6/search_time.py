import random
import time

def generate_random_array(x, size):
    for i in range(size):
        x.append(random.randint(-100000, 100000))

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
    generate_random_array(x, 200000)
    y = []
    copy(x, y)
    y.sort()    #y is sorted to perform binary search
    #start time is noted
    start = time.time()
    for i in range(2000):
        temp = random.randint(-100000, 100000)
        linear_search(x, temp)
    #finish time is noted
    finish = time.time()
    print(f'Time taken by linear search: {float(finish - start)}')
    start = time.time()
    for i in range(2000):
        temp = random.randint(-100000, 100000)
        binary_search(x, temp)
    finish = time.time()
    print(f'Time taken by binary search: {float(finish - start)}')
main()
