def reverse_string(string,i):
    if i == 0:
        print(string[i])
        return
    print(string[i],end=' ')
    reverse_string(string,i-1)

import random as r
def main():
    string = input()
    list = [j for j in range(2)]
    reverse_string(string,len(string)-1)
    reverse_string(list,len(list)-1)

main()
