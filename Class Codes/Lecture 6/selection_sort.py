import random

def generate_random_array(x, size):
    for i in range(size):
        x.append(random.randint(1,99))

def find_min_index(x, start):
    min_index = start
    for i in range(start+1, len(x)):
        if x[i] < x[min_index]:
            min_index = i
    return min_index

def selection_sort(x):
    min_index=0
    for i in range(len(x)-1):
        min_index = find_min_index(x, i)
        if min_index != i:
            x[i], x[min_index] = x[min_index], x[i]

def main():
    x=[]
    generate_random_array(x, 20)
    print(x)
    selection_sort(x)
    print(x)

main()
