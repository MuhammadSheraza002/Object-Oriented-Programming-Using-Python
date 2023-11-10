def file3():
    file = open("flood1.txt", mode="r")
    w = file.read()
    for character in w:
        if character == '.':
            print(".")
        else:
            print (character, end='')

file3()
