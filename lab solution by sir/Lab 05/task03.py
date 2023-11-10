def write_file():
    file = open("newfile.txt","w")
    #writing lines in the file.
    words=["One", "Two", "Three", "Four", "Five"]
    for word in words:
        file.write(f'{word}\n')

write_file()
