import random as r

def print_city_max_links(b):
    max_city = 0
    max_links = 0
    for i in range(len(b)):
        link_count = 0
        for j in range(len(b)):
            if b[i][j] == 1:
                link_count += 1
        if max_links < link_count:
            max_links = link_count
            max_city = i
    print (f' City {i} has maximum links')

def main():
    board = [[r.randint(0,1) for i in range(5)] for j in range(5)]
    print(board)
    print_city_max_links(board)

main()
