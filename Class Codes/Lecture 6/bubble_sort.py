import random

def generate_random_array(x, size):
    for i in range(size):
        x.append(random.randint(1,99))

def bublle_elements(x, index):
    for i in range(len(x)-1):
        if x[i+1] < x[i]:
            x[i+1], x[i]=x[i], x[i+1]

def bubble_sort(x):
    for i in range(len(x)):
        bublle_elements(x, i)

def main():
    x=[]
    generate_random_array(x, 20)
    print(x)
    bubble_sort(x)
    print(x)

main()
