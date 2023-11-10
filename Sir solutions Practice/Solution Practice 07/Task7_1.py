import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def print_elements_larger_than_neighbors(x):
    for i in range(1,len(x)-1):
        if x[i] > x[i-1] and x[i] > x[i+1]:
            print (x[i], end=' ')
    print()

def main():
    x=[]
    init_random_list(x)
    print(x)
    print_elements_larger_than_neighbors(x)

main()