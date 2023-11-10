def read_file():
    file = open("sentences.txt","r")
    #reading file line by line.
    for line in file:
        print(f'({len(line)}) ', end='')
        print(line, end='')
    print ("Check count, count is one more than the characters")
    print ("One extra count is due to line feed character, check next program")

read_file()
