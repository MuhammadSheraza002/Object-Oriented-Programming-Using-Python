def q2_2():
    x=[2, 3, 9, 4, 6, 0, 1, 2]
    for i in range(len(x)-2):   #In loop we are using index i+2, therefore in condition, we will add -2
        if x[i] <= x[i+1] and x[i+1] <= x[i+2]:
            print(x[i],'\t',x[i+1],'\t',x[i+2])

q2_2()

