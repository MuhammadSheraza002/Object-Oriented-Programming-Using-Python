def count_numbers(line):
    count = 1
    for w in line:
        if w == ' ' or w == '\n':
            count += 1
    return count

def return_numbers_in_list(file):
    line = file.read()
    count = count_numbers(line)
    arr = [0] * count
    i = 0
    for w in line:
        if w != ' ' and w!='\n':
            arr[i] = arr[i] * 10 + (ord(w)-ord('0'))    #place numbers in the list
        else:
            i += 1
    return arr

def return_numbers_in_list(file):
    line = file.read()
    count = count_numbers(line)
    arr = [0] * count
    i = 0
    for w in line:
        if w != ' ' and w!='\n':
            arr[i] = arr[i] * 10 + (ord(w)-ord('0'))    #place numbers in the list
        else:
            i += 1
    return arr

def write_union_in_file(n1, n2):
    file = open("union.txt", mode="w")
    for n in n1:
        file.write(str(n)+' ')
    for a in n2:
        is_exist = False
        for b in n1:
            if a==b:
                is_exist = True
                break
        if not(is_exist):
            file.write(str(a)+' ')

def write_intersection_in_file(n1, n2):
    file = open("intersection.txt", mode="w")
    for a in n2:
        for b in n1:
            if a==b:
                file.write(str(a)+' ')
                break

def write_n1_difference_n2(n1, n2, name):
    file = open(name, mode="w")
    for a in n1:
        is_exist = False
        for b in n2:
            if a==b:
                is_exist = True
                break
        if not(is_exist):
            file.write(str(a)+' ')

def task3():
    file = open("numbers1.txt", mode="r")
    n1 = return_numbers_in_list(file)
    file = open("numbers2.txt", mode="r")
    n2 = return_numbers_in_list(file)
    write_union_in_file(n1, n2)
    write_intersection_in_file(n1, n2)
    write_n1_difference_n2(n1, n2,"n1-n2.txt")
    write_n1_difference_n2(n2, n1,"n2-n2.txt")

task3()
