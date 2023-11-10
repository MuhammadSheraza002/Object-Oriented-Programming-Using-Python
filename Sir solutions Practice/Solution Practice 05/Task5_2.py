import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def rotate_larger_element_to_right(x, y):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
            y[i], y[i+1] = y[i+1], y[i]

def bubble_sort(x,y):
    for i in range(len(x)-1):
        rotate_larger_element_to_right(x,y)

def main():
    x=[]
    init_random_list(x)
    y=[]
    init_random_list(y)
    print(f'{x}\n{y}\n')
    bubble_sort(x, y)
    print(f'{x}\n{y}\n')
    bubble_sort(y, x)
    print(f'{x}\n{y}\n')

main()