def has22(array):
    for index in range(len(array)-1):
        if array[index] == 2:
            if array[index+1] == 2:
                return True
    return False

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))