def main():
    list = [1,2,45,5,6,6,76,786,7,3,4]
    greatest_sum = list[0] + list[2]
    for index in range(2,len(list)-1):
        sum = list[index] + list[index+1]
        if greatest_sum < sum:
            greatest_sum = sum
    print(greatest_sum)


main()

