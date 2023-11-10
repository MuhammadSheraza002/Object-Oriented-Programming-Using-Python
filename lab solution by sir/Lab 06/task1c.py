def place(list2d, list1d, i, j, rows, columns):
    c = 0
    for element in list1d:
        list2d[i][j+c] = element
        c += 1
        if c ==  columns:
            c = 0
            i += 1

def main():
    a =[1, 2, 3, 4, 5, 6]
    b =[[11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
    place(b, a, 1, 2, 3, 2)
    print(b)

main()

