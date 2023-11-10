def sum13(array):
    if array == []:
        return 0
    sum_of_array = 0
    for index in range(len(array)):
        if array[index] == 13:
            index+=1
            continue
        sum_of_array += array[index]
    return sum_of_array

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))