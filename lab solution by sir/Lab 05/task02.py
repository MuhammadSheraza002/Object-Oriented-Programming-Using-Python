def read_file():
    file = open("sentences.txt","r")
    #reading file line by line.
    for line in file:
        for character in line:
            print(f'{ord(character)} ', end='')
        print(line, end='')
    print ("We hav printed ASCII codes and you can see 10 <line feed character> at the end of every line")

read_file()
