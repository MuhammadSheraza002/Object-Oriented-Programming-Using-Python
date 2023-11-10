import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def rotate_larger_element_to_right(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]

def bubble_sort(x):
    for i in range(len(x)-1):
        rotate_larger_element_to_right(x)

def main():
    x=[]
    init_random_list(x)
    print(x)
    bubble_sort(x)
    print(x)

main()