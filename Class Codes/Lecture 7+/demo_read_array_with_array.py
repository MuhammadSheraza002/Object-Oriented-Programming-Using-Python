import random as r

def demo_read_array_with_array():
    x = [23, 36, 45, 12, 18, 29, 32]
    y = [3, 4, 0, 5, 6, 1, 2]           #y has sorted index on x
    for i in range(len(y)):
        print(x[y[i]], end=' ')
    print()


demo_read_array_with_array()
