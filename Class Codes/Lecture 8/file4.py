def file4():
    file = open("flood1.txt", mode="r")
    text = file.read()
    for i in range(len(text)):
        if text[i] == '.':
            print(".")
        elif text[i]!=' ':
            print (text[i], end='')
        elif text[i]==' ' and text[i-1]!='.':
            print (text[i], end='')

file4()
