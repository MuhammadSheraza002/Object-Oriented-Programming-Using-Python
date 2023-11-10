def count_numbers(line):
    count = 1
    for w in line:
        if w == ' ' or w == '\n':
            count += 1
    return count

def file1():
    file = open("data.txt", mode="r")
    line = file.read()
    print (line)
    count = count_numbers(line) #count numbers in the file
    arr = [0] * count           #declare list according to the count
    i = 0
    for w in line:
        if w != ' ' and w!='\n':
            arr[i] = arr[i] * 10 + (ord(w)-ord('0'))    #place numbers in the list
        else:
            i += 1
    print (arr)
    print (sum(arr))
file1()
