def upper_triangle():
    list = [[98, 62, 66, 40, 90],
            [59, 79, 31, 38, 92],
            [70, 72, 48, 50, 29],
            [97, 17, 72, 53, 41],
            [66, 22, 36, 36, 50]]

    rows = 5
    cols = 5
    end = 0
    for row in range(rows):
        for col in range(cols-end):
            print(list[row][col],end=' ')
        print()
        end+=1


upper_triangle()


