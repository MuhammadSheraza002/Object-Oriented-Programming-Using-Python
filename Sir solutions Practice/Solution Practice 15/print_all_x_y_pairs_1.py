import random as r

def print_all_x_y_pairs(list, x=0, y = 1):
    if x == len(list)-1:    #No pair left as x is pointing to last element, therefore return
        return
    if y == len(list):      #all x, y pairs are printed
        print_all_x_y_pairs(list, x+1, x+2) #Call function with next x to print pairs
        if x < len(list) - 2:        print()     #for line break only if last pair is not printed
        return
    print_all_x_y_pairs(list, x, y+1)           #call function for next y element to be paired with x
    print (f'({list[x]}, {list[y]})', end=' ')#print current pair
    if x==0 and y==1:   print() #move to next line

def main():
    x = [r.randint(1,9) for i in range(5)]
    print (x)
    print ('---------------')
    print_all_x_y_pairs(x)

main()
