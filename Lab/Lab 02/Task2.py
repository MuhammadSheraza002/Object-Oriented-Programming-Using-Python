import random

def main():
    print("Enter date by input dd, mm && yyyy in next three lines")
    d = int(input("DD: "))
    m = int(input("MM: "))
    y = int(input("YYYY: "))
    if d < 0 or m < 0 or y < 0:
        print ("Invalid Date")
    elif m > 12 or y < 1000:
        print ("Invalid Date")
    elif ( m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d <= 31:
        print ("Valid Date")
    elif ( m == 4 or m == 6 or m == 9 or m == 11) and d <= 30:
        print ("Valid Date")
    else:
        if d > 29:
            print ("Invalid Date")
        elif d==29 and (y % 4 != 0 or (y % 100 == 0 and y % 400 != 0)):
            print ("Invalid Date")
        else:
            print ("Valid Date")
            
main()
