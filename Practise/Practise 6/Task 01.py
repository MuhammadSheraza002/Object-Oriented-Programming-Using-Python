import random

def count_frequency(list):
    count = [0] * (11)
    for index in range(len(list)):
        count[list[index]] +=1

    i = 0
    for index in range(len(count)):
        for j in range(count[index]):
            list[i] = index
            i+=1

def frequency_of_each_number():
    size = random.randint(15,20)
    list = [random.randint(0,10) for i in range(size)]
    print(list)
    count_frequency(list)
    print(list)

frequency_of_each_number()