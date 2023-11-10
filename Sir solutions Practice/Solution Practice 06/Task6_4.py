import random as r

def print_upper_triangle(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if i <= j:
                print (x[i][j], end= ' ')
            else:
                print('  ', end = ' ')
        print()

def main():
    x=[[r.randint(10, 99) for i in range(5)] for j in range(5)]
    print(x)
    print_upper_triangle(x)

main()