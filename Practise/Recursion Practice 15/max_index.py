def max_index(list,max,maximum_index,i=0):
    if i == len(list):
        return maximum_index
    if max < list[i]:
        max = list[i]
        maximum_index=i
    return max_index(list,max,maximum_index,i=i+1)

import random as r

def main():
    list = [r.randint(10,50) for i in range(5)]
    print(list)
    print(max_index(list,list[0],0))

main()
