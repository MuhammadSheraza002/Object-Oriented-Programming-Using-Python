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

def main():
    x=[]
    init_random_list(x)
    print(x)
    check_and_count_out_of_order_pairs(x)

main()
