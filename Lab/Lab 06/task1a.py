def print_row_column_form(arr, rows, columns):
    c = 0
    for element in arr:
        print (element, end=' ')
        c += 1
        if c ==  columns:
            c = 0
            print()


def main():
    a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print_row_column_form(a, 3, 4)

main()
