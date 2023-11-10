#Find sum of all elements of list

def sum_of_list(list,i = 0,sum=0):
    if i == len(list):
        return sum
    return sum_of_list(list,i=i+1,sum=sum+list[i])

import random as r

def main():
    list = [r.randint(1,3) for i in range(5)]
    print(list)
    print(sum_of_list(list))

main()