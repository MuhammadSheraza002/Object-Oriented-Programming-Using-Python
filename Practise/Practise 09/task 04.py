def list_print():
    list = [
        [1,2,3],
        [4,5,6,],
        [7,8,9],
        ]
    for i in range(len(list)-1,-1,-1):
        for j in range(len(list)-1,-1,-1):
            print(list[i][j],end=' ')
        print()
    print()
    print("<________>")
    for i in range(len(list)):
        for j in range(len(list)):
            print(list[i][j],end=' ')
        print()

list_print()