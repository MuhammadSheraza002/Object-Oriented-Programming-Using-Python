def main():
    #in windows complete path may not required, however, it is required in Linux according to my settings
    file1 = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text.txt','r')
    file2 = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text_copy.txt','w+')
    file2.write(file1.read())
    file1.close()
    file2.close()

main()