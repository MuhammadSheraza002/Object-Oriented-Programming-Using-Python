file = open('fifa.csv', 'r')
heading = file.readline()
for i in range(32):
    string = file.readline().strip()
    print(string)
