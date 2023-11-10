import random

def main():
    amount = int(input("Enter Amount Rounded in Hundreds:"))
    five_thousand = amount // 5000
    amount = amount % 5000
    one_thousand = amount // 1000
    amount = amount % 1000
    five_hundred = amount // 500
    amount = amount % 500
    one_hundred = amount // 100
    amount = amount % 100
    fifty = amount // 50
    amount = amount % 50
    ten = amount // 10
    if five_thousand > 1:
        print (five_thousand, " five thousand notes")
    elif five_thousand == 1:
        print (five_thousand, " five thousand note")
    if one_thousand > 1:
        print (one_thousand, " one thousand notes")
    elif one_thousand == 1:
        print (one_thousand, " one thousand note")
    if five_hundred > 0:
        print (five_hundred, " five hundred note")
    if one_hundred > 1:
        print (one_hundred, " one hundred notes")
    elif one_hundred == 1:
        print (one_hundred, " one hundred note")
    if fifty > 0:
        print (fifty, " fifty rupee note")
    if ten > 1:
        print (ten, " ten rupee notes")
    elif ten == 1:
        print (ten, " ten rupee note")
main()
