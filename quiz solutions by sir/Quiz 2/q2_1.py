def q2_2():
    x=[2, 3, 9, 4, 6, 5, 1, 2]
    average = 4
    for i in range(len(x)):
        if x[i] < average:
            print(x[i], end=' ')
    print()
    for i in range(len(x)):
        if x[i] > average:
            print(x[i], end=' ')
    print()

q2_2()

