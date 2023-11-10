import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def swap_random_pairs_n_times(x, n):
    for i in range(n):
        i = r.randint(0, len(x)-1)
        j = r.randint(0, len(x)-1)
        if i != j:
            x[i], x[j] = x[j], x[i]

def main():
    x=[]
    init_random_list(x)
    print(x)
    swap_random_pairs_n_times(x, 50)
    print(x)

main()