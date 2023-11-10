def read_file_and_print_numbers_only(file):
    for line in file:
        for c in line:
            if c >= '0' and c <= '9':
                print(c, end='')
    print()

def main():
    #in windows complete path may not required, however, it is required in Linux according to my settings
    file = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text.txt','r')
    read_file_and_print_numbers_only(file)
    file.close()

main()