def min_no_of_list(list):
    minimum_number = list[0]
    for index in range(len(list)):
        if list[index] < minimum_number:
            minimum_number = list[index]
    return minimum_number

def main():
    list = [37, 90, 42, 84, 79, 97, 34, 31, 10, 59, 83, 64, 21, 74, 15, 56, 19, 46, 25, 13]
    min_number = min_no_of_list(list)
    for index in range(len(list)):
        list[index] = list[index]-min_number
    print(list)
main()
