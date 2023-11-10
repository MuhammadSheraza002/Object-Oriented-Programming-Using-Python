'''def friend_fashion(you,friend):
    if you>=8 or friend>=8:
        if you<=2 or friend<=2:
            return 0
        return 2
    return 1'''
def friend_fashion(you,friend):
    if you>2 and friend>2:
        if you>=8 or friend>=8:
            return 2
        return 1
    return 0

def main(number1,number2):
    if friend_fashion(number1,number2)==0:
        print("No")
    if friend_fashion(number1,number2)==1:
        print("May be")
    elif friend_fashion(number1,number2)==2:
        print("Yes")
main(int(input("Enter no: ")),int(input("Enter no: ")))