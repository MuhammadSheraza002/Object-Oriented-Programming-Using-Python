import random as r

def init_random_list(x, count):
    for i in range(count):
        x.append(r.randint(10,99))

def is_perfect_square(x):
    limit = int(x/2)+1
    for i in range(limit):
        if i*i == x:
            return True
    return False

def print_perfect_square_elements(x):
    for element in x:
        if is_perfect_square(element):
            print(element)

def main():
    x=[]
    init_random_list(x,30)
    print(x)
    print_perfect_square_elements(x)

main()