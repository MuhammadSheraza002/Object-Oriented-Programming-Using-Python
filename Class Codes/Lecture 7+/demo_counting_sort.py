import random as r

def counting_sort(list, max_element):  #assuming values starts from 0 and ends on max_element
    counts = [0 for i in range(max_element+1)]
    for i in range(len(list)):
        counts[list[i]] += 1
    k = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            list[k] = i
            k  += 1

def demo_counting_sort():
    size = r.randint(15, 20)
    list = [r.randint(0,6) for i in range(size)]
    print(list)
    counting_sort(list, 6)
    print(list)

demo_counting_sort()