import random as r

def display_principal_diagonal(my_list, size):
    for i in range(size):
        print(f'{my_list[i][i]} ',end='')
    print()

def display_secondary_diagonal(my_list, size):
    j = size - 1
    for i in range(size):
        print(f'{my_list[i][j]} ',end='')
        j = j - 1
    print()

def two_dimension_3():
    size = 5
    arr =[ [ r.randint(1,9) for i in range(size)] for j in range(size)]
    display_principal_diagonal(arr, size)
    print ("******************")
    display_secondary_diagonal(arr, size)

two_dimension_3()

