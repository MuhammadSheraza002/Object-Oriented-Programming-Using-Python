def read_file(file):
    for line in file:
        print(line)

def main():
    #in windows complete path may not required, however, it is required in Linux according to my settings
    file = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text.txt','r')
    read_file(file)
    file.close()

main()