import random as r

def insert_in_order(x, y, index):
    temp = x[index]
    i = index - 1
    while i>=0 and y[x[i]]>y[temp]:
        x[i], x[i+1] = x[i+1], x[i]
        i = i - 1
    x[i+1]=temp

def insertion_sort(index, x):
    for i in range(1,len(index)):
        insert_in_order(index, x, i)

def print_arrays_with_index_array(x, index):
    for i in range(len(index)):
        print (x[index[i]], end=' ')
    print()

def demo_parallel_arrays():
    size = 10
    a = [ r.randint(10,99) for i in range(size)]
    b = [ r.randint(10,99) for i in range(size)]
    c = [ r.randint(10,99) for i in range(size)]
    d = [ r.randint(10,99) for i in range(size)]
    print("Before Sorting:")
    print(a)
    print(b)
    print(c)
    print(d)
    a_index =[i for i in range(size)]   #List A has indexes from 0 to size-1
    print(a_index)
    insertion_sort(a_index, a)          #a_index is sorted on the basis of a
    print(a_index)
    print ("A, B, C, D is printed again, please verify column values:")

    print_arrays_with_index_array(a, a_index)   #printing a with respect a_index
    print_arrays_with_index_array(b, a_index)
    print_arrays_with_index_array(c, a_index)
    print_arrays_with_index_array(d, a_index)

demo_parallel_arrays()



