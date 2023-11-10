import random as r

NONE = -1  #constants to have value of negative one

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

def find_and_print_element_having_most_occurences(x):
    max_count = 1
    element_having_most_occurences = x[0]
    for i in range(len(x)):
        count = 1
        if x[i] != NONE:
            for j in range(i+1, len(x)):
                if x[i] != NONE and x[i] == x[j]:
                    count += 1
                    x[j] = NONE
            if count > max_count:
                max_count = count
                element_having_most_occurences = x[i]
    print (f'{element_having_most_occurences} {max_count} times')

def main():
    x=[]
    init_random_list(x)
    print(x)
    y = [element for element in x]  #making a copy of x, to keep x in its original form and change y in next statement
    find_and_print_element_having_most_occurences(y)

main()