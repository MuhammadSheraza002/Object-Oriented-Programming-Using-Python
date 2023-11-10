def average_3_by_3(list):
    for i1 in range(len(list)-2):
        for i2 in range(len(list)-2):
            sum =0
            for i3 in range(i1,i1+3):
                for i4 in range(i2, i2 + 3):
                    sum+=list[i3][i4]
            print(sum/9)
import random
def main():
    list = [[random.randint(0,99) for i in range(5)] for i in range(5)]
    print(list)
    average_3_by_3(list)

main()