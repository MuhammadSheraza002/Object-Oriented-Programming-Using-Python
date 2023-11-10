import random as r

def display_non_zero(my_list, rows, columns):
    for row in my_list:
        for element in row:
            if element != 0:
                print(f'{element} ',end='')
            else:
                print ('  ', end='')
        print()

def two_dimension_4():
    rows = 5
    columns = 6
    arr =[ [ r.randint(0,9) for i in range(columns)] for j in range(rows)]
    display_non_zero(arr, rows, columns)
    print ("******************")


two_dimension_4()

