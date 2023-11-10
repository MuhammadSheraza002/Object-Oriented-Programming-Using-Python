def count_number_out_of_order(list):
    count = 0
    for index in range(len(list)-1):
        if list[index] > list[index+1]:
            print(list[index],list[index+1])
            count += 1
    print(count)
count_number_out_of_order([2,3,3,3,4,3,5,3,45,43,5,6,4,565,55,55])