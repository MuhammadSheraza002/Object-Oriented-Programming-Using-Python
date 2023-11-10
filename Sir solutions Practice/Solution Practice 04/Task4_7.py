import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def find_highest_sum_adjacent_pair(x):
    #assuming array has at least two elements that makes one pair
    highest_sum = x[0]+x[1]
    highest_pair_position=0
    for i in range(1, len(x)-1):
        sum = x[i] + x[i+1]
        if sum > highest_sum:
            highest_sum = sum
            highest_pair_position = i
    print (f'Pair ({x[highest_pair_position]}, {x[highest_pair_position+1]}) has highest sum = {highest_sum}')

def main():
    x=[]
    init_random_list(x)
    print(x)
    find_highest_sum_adjacent_pair(x)

main()
