def binary_search(list,element,start=0,end=6):
    middle = int((start+end)/2)
    if list[middle] == element:
        return middle
    elif element > list[middle]:
        end=end-1
    elif element > list[middle]:
        start=start+1
    elif start > end:
        return middle
    return binary_search(list,element,start,end)

def main():
    list = [1,2,3,4,5,6]
    print(binary_search(list,2))

main()