import random as r

def init_random_list(x, count):
    for i in range(count):
        x.append(r.randint(10,99))

def bubble_sort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

def merge(x, y):
    z = []
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    if i < len(x):
        while i < len(x):
            z.append(x[i])
            i += 1
    else:
        while j < len(x):
            z.append(y[j])
            j += 1
    return z

def main():
    x= []
    init_random_list(x,10)
    bubble_sort(x)
    print(x)
    y= []
    init_random_list(y,10)
    bubble_sort(y)
    print(y)
    z = merge(x, y)
    print(z)

main()
