import random as r

def init(my_list, rows, columns):  #list is two dimensional
    for i in range(rows):
        for j in range(columns):
            my_list[i][j] = r.randint(1,100)

def display(my_list, rows, columns):
    for row in my_list:
        for ele in row:
            print(f'{ele} ',end='')
        print()

def two_dimension_1():
    rows = 5
    columns = 8
    arr1 = [[0] * columns for i in range(rows)]
    init(arr1, rows, columns)
    display(arr1, rows, columns)

    print("***************")
    rows = 4
    columns = 3
    #second syntax to declare & initialize 2D list at random
    arr2 =[ [ r.randint(1,100) for i in range(columns)] for j in range(rows)]
    display(arr2, rows, columns)


two_dimension_1()
