import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def shuffle_elements_by_random_pair_swap(x, n):
    for i in range(n):
        i = r.randint(0, len(x)-1)
        j = r.randint(0, len(x)-1)
        if i != j:
            x[i], x[j] = x[j], x[i]

def main():
    x=[]
    init_random_list(x)
    y=[]
    init_random_list(y)
    print(x)
    shuffle_elements_by_random_pair_swap(x, 100)
    print(x)

main()