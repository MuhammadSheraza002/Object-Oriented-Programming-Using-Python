def read_file_and_count_number_of_words(file):
    count_words = 0
    for line in file:
        for c in line:
            if c == ' ' or c == '\n':
                count_words +=1
    print(f'Total words are: {count_words}')

def main():
    #in windows complete path may not required, however, it is required in Linux according to my settings
    file = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text.txt','r')
    read_file_and_count_number_of_words(file)
    file.close()

main()