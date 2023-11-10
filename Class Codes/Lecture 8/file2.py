def file2():
    file = open("flood.txt", mode="r")
    w = file.read()
    print (w)
    print (f'No of words in file: {len(w)}')

file2()

