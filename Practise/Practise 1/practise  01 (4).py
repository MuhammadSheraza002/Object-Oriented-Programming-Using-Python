def sum67(list):
    sum_of_list = 0
    for index in range(len(list)):
        if list[index] == 6:
            index = list.index(7) + 1
            while index < len(list):
                sum_of_list += list[index]
                index+=1
            return sum_of_list
        sum_of_list += list[index]

    return sum_of_list

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))