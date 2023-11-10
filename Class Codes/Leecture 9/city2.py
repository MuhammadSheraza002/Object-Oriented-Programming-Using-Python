import random as r

def show_link_count(b):
    for i in range(len(b)):
        count = 0
        for j in range(len(b)):
            if b[i][j] == 1:
                count += 1
        print (f' City {i} has {count} links')

def main():
    board = [[r.randint(0,1) for i in range(10)] for j in range(10)]
    print(board)
    show_link_count(board)

main()
