from random import randint
def main():
    list = [37, 90, 42, 84, 79, 97, 34, 31, 10, 59, 83, 64, 21, 74, 15, 56, 19, 46, 25, 13]
    index1 = randint(0,len(list))
    index2 = randint(0,len(list))
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    print(index1)
    print(index2)
    print(list)

main()
