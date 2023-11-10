'''initialize = 1
for row in range(1,6):
    sum = 0
    for column in range(row):
        sum += initialize
        print(initialize,end=' ')
        initialize += 1
    print(" = %d"%(sum))


'''

i = 1
while i <= 15:
    sum = 0
    row = 1
    while row<=i:
        print(i,end=' ')
        sum+=i
        row+=1
    i+=1

    print('= ', sum)
