def swapping(list,i1,i2):
    list[i1],list[i2] = list[i2],list[i1]
    return list

def smallest_index(list):
    small = list[0]
    small_index = 0
    for index in range(len(list)):
        if list[index]<small:
            small=list[index]
            small_index = index
    return small_index

def next_small_index(list,smallest_index,start_index):
    smallest = list[smallest_index]
    second_small = list[start_index]
    smaller_index = start_index
    for index in range(start_index,len(list)):
        if list[index] < second_small and list[index]>smallest:
            second_small = list[index]
            smaller_index = index
    return smaller_index

def selection_sort(list):
    swapping(list,0,smallest_index(list))
    small_index = smallest_index(list)
    for index in range(1,len(list)):
        small_index = next_small_index(list,small_index,index)
        swapping(list,index,small_index)

import random as r

def main():
    list = [r.randint(0,99) for i in range(10)]
    print("random list: ",list)
    selection_sort(list)
    print(list)

main()