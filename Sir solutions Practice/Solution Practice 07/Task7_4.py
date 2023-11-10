import random as r

def init_random_list(x, count):
    for i in range(count):
        x.append(r.randint(10,99))

#Function has to print elements of x with the count of smaller elements in y
def print_element_x_with_count(x, y):
    for element1 in x:
        count = 0
        for element2 in y:
            if element1 > element2:
                count += 1
        print(f'({element1} {count})')

def main():
    x=[]
    init_random_list(x,5)
    print(x)
    y=[]
    init_random_list(y,10)
    print(y)
    print_element_x_with_count(x, y)

main()