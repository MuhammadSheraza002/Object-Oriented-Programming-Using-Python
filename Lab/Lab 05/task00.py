def read_file():
    file = open("sentences.txt","r")
    #reading file line by line.
    for line in file:
        print(line, end='')

read_file()
