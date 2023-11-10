def difference_of_list(min_list,max_list):
    max = max_list[0] - min_list[0]
    index = 0
    for i in range(len(max_list)):
        if max < max_list[i] - min_list[i]:
            max = max_list[i] - min_list[i]
            index = i
    return index



def main():
    list = [2,3,4,2,3,32,64,3,45]
    min_list = []
    max_list = []
    min = 0
    max = 0
    index = 0
    while index < len(list)-1:

        if list[index] < list[index+1]:
            min = index
            max= 0

            while list[index] < list[index+1] and index < len(list)-2:
                max = index+1
                index+=1
            min_list.append(min)
            max_list.append(max)
        index+=1


    I = difference_of_list(min_list,max_list)
    print(I)
    i1 = min_list[I]
    print(i1)
    i2 = max_list[I]
    print(i2)
    print(list[i1:i2+1])




main()

