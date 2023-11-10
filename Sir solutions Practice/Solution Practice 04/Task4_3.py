import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def find_index_of_minimum_element(x):
    min_element_index = 0
    for i in range(1, len(x)):
        if x[min_element_index] > x[i]:
            min_element_index = i
    return min_element_index

def subtract_min_from_list(list, min_element):
    for i in range(len(list)):
        list[i] -= min_element

def main():
    x=[]
    init_random_list(x)
    print(x)
    subtract_min_from_list(x, x[find_index_of_minimum_element(x)])
    print(x)

main()