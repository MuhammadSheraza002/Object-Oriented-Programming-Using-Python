import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def bubble_sort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

def is_larger_from_left_side_elements(x, position):
    for i in range (position-1):
        if x[i] >= x[position]:
            return False
    return True

def is_smaller_from_right_side_elements(x, position):
    for i in range (position+1, len(x)):
        if x[i] <= x[position]:
            return False
    return True

def print_elements_in_position(x):
    for i in range(len(x)-1):
        if is_larger_from_left_side_elements(x, i) and is_smaller_from_right_side_elements(x,i):
            print (x[i], end=' ')
    print()

def main():
    x=[]
    init_random_list(x)
    print(x)
    print_elements_in_position(x)
    #after sort only equal elements will not be printed
    bubble_sort(x)
    print_elements_in_position(x)
main()