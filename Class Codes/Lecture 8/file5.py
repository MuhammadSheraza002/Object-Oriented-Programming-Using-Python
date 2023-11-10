def file5():
    file = open("data1.txt", mode="r")
    line = file.read()
    arrs = line.split(" ")  #In case of split, we can have only one delimeter, whereas in my code I have used two delimeters.
    print(arrs)
    for i in range(len(arrs)):
        arrs[i] = int(arrs[i])
    print(arrs)

file5()

