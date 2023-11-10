def q2_3_():
    x=[23, 34, -1, 45, 12, 18, -1, 25, 36]
    reverse = []
    for i in range(len(x)):
        if x[i]!=-1:
            reverse.append(x[i])
        else:
            print(reverse[::-1])
            reverse = []
        if i==len(x)-1 and x[i]!=-1:
            print(reverse[::-1])

def q2_3():
    #First method
    x=[23, 34, -1, 45, 12, 18, -1, 25, 36]
    start = 0
    for i in range(len(x)):
        if x[i]==-1 or i == len(x) - 1:
            end = i - 1
            if i == len(x) - 1:
                end = i
            for j in range(end, start-1, -1):
                print(x[j], end=' ')
            start = i + 1
            print()
    print('----------------')
    #Second method
    q2_3_()

q2_3()

