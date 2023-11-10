import random as r

def init(my_list, rows, columns):  #list is two dimensional
    for i in range(rows):
        for j in range(columns):
            my_list[i][j] = r.randint(1,9)

def display(my_list, rows, columns):
    for row in my_list:
        for ele in row:
            print(f'{ele} ',end='')
        print()

def display_column_wise(my_list, rows, columns):
    for i in range(columns):
        for j in range(rows):
            print(f'{my_list[j][i]} ',end='')
        print()

def find_row_sum(my_list, row, columns):
    sum = 0
    for i in range(columns):
        sum = sum + my_list[row][i]
    return sum

def two_dimension_2():
    rows = 3
    columns = 5
    arr =[ [ r.randint(1,9) for i in range(columns)] for j in range(rows)]
    init(arr, rows, columns)
    display(arr, rows, columns)
    print ("******************")
    display_column_wise(arr, rows, columns)
    print(f'Sum of third row:{find_row_sum(arr, 2, columns)}')

two_dimension_2()
