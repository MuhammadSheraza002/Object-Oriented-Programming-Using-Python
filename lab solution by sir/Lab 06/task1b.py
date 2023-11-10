def convert(arr, rows, columns):
    new_list=[[0 for i in range(columns)]for j in range(rows)]
    r = 0
    c = 0
    for element in arr:
        new_list[r][c] = element
        c += 1
        if c ==  columns:
            c = 0
            r += 1
    return new_list


def main():
    a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    b = convert(a, 3, 4)
    print(b)

main()
