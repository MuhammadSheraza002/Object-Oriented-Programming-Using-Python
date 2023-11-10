import random as r

def insert_in_order(list1, list2, index):
    temp = list1[index]
    temp_y = list2[index]
    i = index - 1
    while i>=0 and list1[i]>temp:
        list1[i+1] = list1[i]
        list2[i+1] = list2[i]
        i = i - 1
    list1[i+1]=temp
    list2[i+1]=temp_y

def insertion_sort(list1, list2):
    for i in range(1,len(list1)):
        insert_in_order(list1, list2, i)

def binary_search(list1, element):
    start = 0
    end = len(list1) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if list1[middle] == element:
            return middle
        elif list1[middle] > element:
            end = middle - 1
        else:
            start = middle + 1
    return -1

def demo_parallel_array1():
    size = r.randint(15, 20)
    list1 = [ r.randint(10,99) for i in range(size)]
    list2 = [ r.randint(10,99) for i in range(size)]
    print("Before Sorting:")
    print(list1)
    print(list2)
    insertion_sort(list1, list2)
    print("After Sorting:")
    print(list1)
    print(list2)
    while (True):
        index = binary_search(list1, r.randint(10,99))
        if index != -1:
            print(f'{list1[index]}, {list2[index]}')
            break
    #Now making a copy of lists
    a=[0]*size
    b=[0]*size
    a=[list1[i] for i in range(len(list1))]
    b=[list2[i] for i in range(len(list2))]
    print("Before Sorting:")
    print(a)
    print(b)
    insertion_sort(b, a)
    print("After Sorting:")
    print(a)
    print(b)
#now search in b and display corresponding element of both a & b
    while (True):
        index = binary_search(b, r.randint(10,99))
        if index != -1:
            print(f'{a[index]}, {b[index]}')
            break

demo_parallel_array1()
