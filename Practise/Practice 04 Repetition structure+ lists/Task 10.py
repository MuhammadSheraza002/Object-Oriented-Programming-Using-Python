
def main():
    array = [i for i in range(2, 100)]
    for i in range(2,len(array),2):
        array[i] = -1
    for i in range(4,len(array),3):
        array[i] = -1
    for i in range(8,len(array),5):
        array[i] = -1
    for i in range(12,len(array),7):
        array[i] = -1

    for i in range(len(array)):
        if array[i] != -1:
            print(array[i])
    print(array)
main()