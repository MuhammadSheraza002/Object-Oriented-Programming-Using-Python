import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def find_sum(x):
    sum = 0
    for element in x:
            sum += element
    return sum

def check_and_print_elements_less_than_average(list):
    average = find_sum(list)/len(list)
    count = 0
    for element in list:
        if element < average:
            count += 1
    print (f'{count} elements are smaller than average')

def main():
    x=[]
    init_random_list(x)
    print(x)
    check_and_print_elements_less_than_average(x)

main()