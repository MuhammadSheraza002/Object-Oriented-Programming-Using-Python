import random

def main():
    n = random.randint(0, 99)
    print (n,end="\t")
    digit1 = n // 10
    digit2 = n % 10
    if n < 20:
        if n == 0:
            print ("zero")
        elif n == 1:
            print ("one")
        elif n == 2:
            print ("two")
        elif n == 3:
            print ("three")
        elif n == 4:
            print ("four")
        elif n == 5:
            print ("five")
        elif n == 6:
            print ("six")
        elif n == 7:
            print ("seven")
        elif n == 8:
            print ("eight")
        elif n == 9:
            print ("nine")
        elif n == 10:
            print ("ten")
        elif n == 11:
            print ("eleven")
        elif n == 12:
            print ("twelve")
        elif n == 13:
            print ("thirteen")
        elif n == 14:
            print ("fourteen")
        elif n == 15:
            print ("fifteen")
        elif n == 16:
            print ("sixteen")
        elif n == 17:
            print ("seventeen")
        elif n == 18:
            print ("eighteen")
        elif n == 19:
            print ("nineteen")
        return
    if digit1 == 2:
        print ("twenty ", end="")
    elif digit1 == 3:
        print ("thirty ", end="")
    elif digit1 == 3:
        print ("thirty ", end="")
    elif digit1 == 4:
        print ("fourty ", end="")
    elif digit1 == 5:
        print ("fifty ", end="")
    elif digit1 == 6:
        print ("sixty ", end="")
    elif digit1 == 7:
        print ("seventy ", end="")
    elif digit1 == 8:
        print ("eighty ", end="")
    elif digit1 == 9:
        print ("ninety ", end="")
    #
    if digit2 == 0:
        print ("")
    elif digit2 == 1:
        print ("one")
    elif digit2 == 2:
        print ("two")
    elif digit2 == 3:
        print ("three")
    elif digit2 == 4:
        print ("four")
    elif digit2 == 5:
        print ("five")
    elif digit2 == 6:
        print ("six")
    elif digit2 == 7:
        print ("seven")
    elif digit2 == 8:
        print ("eight")
    else:
        print ("nine")

main()
