import random

def generate_random_array(x, size):
    for i in range(size):
        x.append(random.randint(1,99))

def insert_in_order(x, index):
    temp = x[index]
    i = index - 1
    while i>=0 and x[i]>temp:
        x[i+1] = x[i]
        i = i - 1
    x[i+1]=temp

def insertion_sort(x):
    for i in range(1,len(x)):
        insert_in_order(x, i)

def main():
    x=[]
    generate_random_array(x, 20)
    print(x)
    insertion_sort(x)
    print(x)

main()
