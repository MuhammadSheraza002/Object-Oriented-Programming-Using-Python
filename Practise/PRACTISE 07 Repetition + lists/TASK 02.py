def counting_lines(file):
    read_file = file.read()
    count =0
    for i in read_file:
        if i=='\n':
            count+=1
    return count

def main():
    file_read = open('test.txt','r')
    #print(file_read.readline())
    i = 0
    while i < counting_lines(file_read):
        file_read.readline()
        i+=1


main()