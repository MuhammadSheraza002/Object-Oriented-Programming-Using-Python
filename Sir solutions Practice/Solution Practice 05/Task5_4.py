import random as r

NONE = -1

#at start list has elements 2-99, later some elements become -1. The function will search from starting position and return next non-negative element
def get_index_of_next_prime(x, start):
    for i in range(start, len(x)):
        if x[i] != NONE:
            return i
    return len(x)

def replace_every_kth_element_with_minus_one(x, start, k):
    for i in range(start, len(x), k):
        x[i] = NONE

def replace_composite_numbers_with_minus_one(x):
    k = 0
    while True:
        k = get_index_of_next_prime(x, k)
        if k == len(x):
            break
        else:
            replace_every_kth_element_with_minus_one(x, k+x[k], x[k])
            k += 1

def print_non_negative(x):
    for element in x:
        if element != NONE:
            print (element, end=' ')
    print()

def main():
    x=[element for element in range(2, 101)]
    print(x)
    replace_composite_numbers_with_minus_one(x)
    print_non_negative(x)

main()