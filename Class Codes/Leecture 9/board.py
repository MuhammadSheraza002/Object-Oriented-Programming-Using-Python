import random as r

def show_link(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == 1:
                print (f' City {i} has link with city {j}')

def main():
    board = [[r.randint(0,1) for i in range(5)] for j in range(5)]
    print(len(board))
    show_link(board)

main()
