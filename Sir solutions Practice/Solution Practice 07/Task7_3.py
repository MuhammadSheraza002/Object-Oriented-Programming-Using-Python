import random as r

def init_random_list(x, count):
    for i in range(count):
        x.append(r.randint(10,99))

def print_pairs(x, y):
    for element1 in x:
        for element2 in y:
            print(f'({element1} {element2})')

def main():
    x=[]
    init_random_list(x,3)
    print(x)
    y=[]
    init_random_list(y,2)
    print(y)
    print_pairs(x, y)

main()