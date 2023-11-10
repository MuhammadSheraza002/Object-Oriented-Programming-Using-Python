def same_index(list,j = 1,i=0):
    if i == len(list):
        return

    if j == len(list) and i < len(list):
        same_index(list, j=i+2, i=i+1)

    elif j < len(list) and i < len(list):
        if list[i] == list[j] and i!=j:
            print(f'{i},{j}')
        same_index(list,j=j+1,i=i)

from random import randint

def main():
    list = [randint(0,10) for i in range(10)]
    print(list)
    same_index(list)
main()