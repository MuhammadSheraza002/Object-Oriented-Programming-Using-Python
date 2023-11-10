import random as r

def print_elements_with_column_sum(x):
    column_sum = [0 for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            print (x[i][j], end='  ')
            column_sum [j] += x[i][j]
        print()
    for element in column_sum:
        print(element, end=' ')
    print()

def main():
    x=[[r.randint(10, 99) for i in range(5)] for j in range(5)]
    print_elements_with_column_sum(x)

main()