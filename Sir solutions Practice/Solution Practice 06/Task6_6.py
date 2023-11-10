import random as r

def print_max_element_with_position_in_each_row(x):
    for i in range(len(x)):
        max_index = 0
        for j in range(1, len(x)):
            if x[i][max_index] < x[i][j]:
               max_index = j
        print(f'Row {i+1}: {x[i][max_index]} at {max_index}')

def main():
    x=[[r.randint(10, 99) for i in range(5)] for j in range(5)]
    print(x)
    print_max_element_with_position_in_each_row(x)

main()