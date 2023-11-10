import random

def counting(list,element):
    count=0
    for i in range(len(list)):
        if element == list[i]:
            count+=1
    return count

def highest_frequency():
    size = random.randint(1,10)
    list = [random.randint(0,10) for i in range(size)]

    max = counting(list,list[0])
    max_index =  0
    for i in range(len(list)):
        if counting(list,list[i]) > max:
            max = counting(list,list[i])
            max_index=i
    print(list)
    print(list[max_index], max, 'times')

highest_frequency()