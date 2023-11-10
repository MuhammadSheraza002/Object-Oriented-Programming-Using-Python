import random as r

def print_elements_with_row_sum(x):
    for i in range(len(x)):
        sum = 0
        for j in range(len(x)):
            print (x[i][j], end=' ')
            sum += x[i][j]
        print(f'Sum {sum}')

def main():
    x=[[r.randint(10, 99) for i in range(5)] for j in range(5)]
    print_elements_with_row_sum(x)

main()