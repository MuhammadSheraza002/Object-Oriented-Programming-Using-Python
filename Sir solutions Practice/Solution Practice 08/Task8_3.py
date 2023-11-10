def read_file_and_display_total_number_of_questions(file):
    count_questions = 0
    for line in file:
        for i in range(len(line)):
            if line[i] >= '0' and line[i] <= '9':       #Quesiton no starts from a digit
                if i < len(line) - 1:
                    if line[i+1] == '.':                #Question no followed by a dot, in case of questions greater than 9 (in two digits), you need some change in code
                        count_questions +=1
    print(f'Total questions are: {count_questions}')

def main():
    #in windows complete path may not required, however, it is required in Linux according to my settings
    file = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text.txt','r')
    read_file_and_display_total_number_of_questions(file)
    file.close()

main()