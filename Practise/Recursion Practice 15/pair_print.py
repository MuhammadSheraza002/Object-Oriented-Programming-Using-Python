def pair_print(list,j=1,i = 0):
    if i == len(list)-1:
        return
    if j == len(list)-1 :
        print(f'({list[i]},{list[j]})')
        pair_print(list,j=i+2,i=i+1)
    elif j < len(list) and i < len(list)-1:
        print(f'({list[i]},{list[j]})',end=',')
        pair_print(list,j=j+1,i=i)


import random as r

def main():
    list = [r.randint(10,50) for i in range(5)]
    print(list)
    pair_print(list)

main()
