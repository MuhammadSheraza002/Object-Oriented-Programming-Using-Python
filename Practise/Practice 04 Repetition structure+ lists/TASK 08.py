import random
def main():
    list = [3,23,6,65,65,45,55,99,22,66]
    for i in range(len(list)):
        for k in range(len(list)):
            count = 0
            number = list[k]
            for j in range(len(list)):
                if list[j] < number:
                    count+=1
            if count==i:
                print(list[k])
                break



main()