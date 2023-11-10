def find_average(list):
    sum_of_list = 0
    for index in range(len(list)):
        sum_of_list+=list[index]
    return sum_of_list/len(list)
def main():
    list =[23,4,5,6,6]
    count = 0
    average = find_average(list)
    for index in range(len(list)):
        if list[index] < average:
            count+=1
    print(average)
    print(count,'elements are smaller than averag')

main()
