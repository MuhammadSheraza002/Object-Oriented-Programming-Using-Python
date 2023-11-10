import random
def main():
    list = [[random.randint(10,40) for i in range(4)] for j in range(4)]
    average_neighour(list)
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

def average_neighour(list):
    for i in range(1,len(list)-1):
        sum = 0
        for j in range(1, len(list)-1):
            sum+=list[i-1][j]
            sum+=list[i+1][j]
            sum+=list[i][j-1]
            sum+=list[i][j+1]
            sum+=list[i-1][j-1]
            sum+=list[i-1][j+1]
            sum+=list[i+1][j+1]
            sum+=list[i+1][j-1]
            print(sum//8,end=' ')
        print()



main()