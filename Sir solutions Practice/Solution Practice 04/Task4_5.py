import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def check_and_count_out_of_order_pairs(x):
    count = 0
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            count += 1
    print (f'{count} pairs are out of order')

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
    check_and_count_out_of_order_pairs(x)
    swap_random_pairs_n_times(x, 50)
    check_and_count_out_of_order_pairs(x)

main()