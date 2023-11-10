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

def find_index_of_maximum_element(x):
    max_element_index = 0
    for i in range(1, len(x)):
        if x[max_element_index] < x[i]:
            max_element_index = i
    return max_element_index


def main():
    x=[]
    init_random_list(x)
    print(x)
    print(x[find_index_of_minimum_element(x):find_index_of_maximum_element(x)+1])

main()