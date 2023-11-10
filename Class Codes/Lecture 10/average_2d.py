import random as r

def average_board(b):
    for i in range(1,len(b)-1):
        for j in range(1,len(b)-1):
            b[i][j] = int((b[i-1][j]+b[i+1][j]+b[i][j+1]+b[i][j-1])/4)

def main():
    board = [[r.randint(0,255) for i in range(5)] for j in range(5)]
    print(board)
    average_board(board)
    print(board)    #no effect on first and last row, first and last column. Only values away from boundary will change

main()
