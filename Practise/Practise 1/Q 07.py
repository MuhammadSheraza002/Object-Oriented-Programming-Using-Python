'''
Input amount from user (amount should be greater than 0
 and in multiples of 10). You have to return the Pakistan's
currency denomination against the amount. For example, if
 user enters 9990, the output should be:
1 five thousand note
4 one thousand notes
1 five hundred note
4 one hundred notes
1 fifty rupee note
4 ten rupee notes
'''
def ten_note(rupee):
    if rupee !=0:
        print(f"{int(rupee)} ten rupee note")
def fifty_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} fifty rupee note")
def one_hundred_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} one hundred rupee note")
def five_hundred_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} five hundred rupee note")
def one_thousand_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} thousand rupee note")
def five_thousand_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} five thousand rupee note")

def Pakistan_currency_denomination():
    amount = int(input("(amount should > 0 and in multiples of 10:  "))
    if amount <= 50:
        if amount == 50:
            fifty_note(1)
        else:
            ten_note(amount / 10)
    elif amount <= 100:
        if amount == 100:
            one_hundred_note(1)
        else:
            fifty_note(1)
            ten_note((amount - 50)//10)
    elif amount <= 500:
        if amount == 500:
            five_hundred_note(1)
        elif amount%100==0:
            one_hundred_note(amount//100)

        else:
            one_hundred_note(amount//100)
            if amount % 100 < 50:
                no_10 = (amount % 100) // 10
                ten_note(no_10)
            elif (amount % 100) == 50:
                fifty_note(1)
            else:
                fifty_note(1)
                no_10 = ((amount % 100) - 50) // 10
                ten_note(no_10)

    elif amount <= 1000:
        if amount == 1000:
            one_thousand_note(1)
        elif amount % 100==0:
            five_hundred_note(1)
            no_100 = (amount - 500) // 100
            one_hundred_note(no_100)
        elif amount > 500 and  amount < 600:
            five_hundred_note(1)
            if amount - 500== 50:
                fifty_note(1)
            if amount - 500 > 50:
                fifty_note(1)
                no_10 = ((amount - 500-50)//10)
                ten_note(no_10)
            if amount - 500 < 50:
                no_10 = ((amount - 500) // 10)
                ten_note(no_10)

        else:
            five_hundred_note(1)
            no_100 = (amount - 500) // 100
            one_hundred_note(no_100)
            if ((amount) % 100) >= 50:
                fifty_note(1)
                if ((amount) % 100) > 50:
                    ten_10 =  (((amount) % 100)-50) // 10
                    ten_note(ten_10)
            else:
                ten_10 = ((amount) % 100) // 10
                ten_note(ten_10)

    elif amount <=5000:
        if amount % 1000  == 0:
            one_thousand_note(amount // 1000)
        elif amount % 1000 >= 500:
            one_thousand_note(amount // 1000)
            five_hundred_note(1)

            if amount % 1000 > 500 and amount % 1000< 600:
                if (amount % 1000) % 100==50:
                    fifty_note(1)
                elif (amount % 1000) % 100 > 50:
                    fifty_note(1)
                    ten_10 =(((amount % 1000) % 100) -50) // 10
                    ten_note(ten_10)
                elif (amount % 1000) % 100<50:
                    ten_10 = (((amount % 1000) % 100)) // 10
                    ten_note(ten_10)
            elif (amount % 1000)>600:
                if (amount % 1000) % 100 ==0:
                    one_hundred_note(((amount % 1000)-500)  // 100)
                elif (amount % 1000) % 100 < 100:
                    if (amount % 1000) % 100 ==50:
                        fifty_note(1)
                    elif (amount % 1000) % 100 > 50:
                        fifty_note(1)
                        ten_note((((amount % 1000) % 100)-50)//10)
                    elif (amount % 1000) % 100 < 50:
                        ten_note(((amount % 1000) % 100)//10)


        elif amount % 1000<500:
            one_thousand_note(amount // 1000)
            if (amount % 1000)<100:
                if (amount % 1000) == 50:
                    fifty_note(1)
                elif (amount % 1000) > 50:
                    fifty_note(1)
                    ten_note(((amount % 1000)-50)//10)
                elif (amount % 1000) < 50:
                    ten_note((amount % 1000) // 10)
            elif (amount % 1000) >= 100 and (amount % 1000) <= 500:
                if (amount % 1000)%100==0:
                    one_hundred_note((amount % 1000)//100)
                else:
                    one_hundred_note((amount%1000)//100)
                    if (amount % 1000)%100 > 50:

                        fifty_note(1)
                        ten_note((((amount % 1000)%100)-50)//10)
                    elif (amount % 1000)%100<50:
                        ten_note(((amount % 1000)%100) // 10)
                    elif (amount % 1000) % 100 == 50:
                        fifty_note(1)

    if amount >= 5000:
        if amount % 5000 == 0:
            five_thousand_note(amount // 5000)
        else:
            five_1000 = amount // 5000
            five_thousand_note(five_1000)
            if (amount % 5000) <= 50:
                if (amount % 5000) == 50:
                    fifty_note(1)
                else:
                    ten_note((amount % 5000)//10)
            elif (amount % 5000) <= 100:
                if (amount % 5000) == 100:
                    one_hundred_note(1)
                elif (amount % 5000) > 50:
                    ten_note((amount % 5000)//10)
                elif (amount % 5000) == 50:
                    fifty_note(1)
                elif (amount % 5000) < 50:
                    ten_note((amount % 5000)//10)
            elif (amount % 5000) <= 500:
                if (amount % 5000) % 100== 0:
                    one_hundred_note((amount % 5000) // 100)
                else:
                    one_hundred_note((amount % 5000) // 100)
                    if (amount % 5000) % 100 == 50:
                        fifty_note(1)
                    elif (amount % 5000) % 100 > 50:
                        fifty_note(1)
                        ten_note((((amount % 5000) % 100)-50)//50)
                    else:
                        ten_note(((amount % 5000) % 100) // 50)
            elif amount % 5000 <= 1000:
                if amount % 5000 == 1000:
                    one_thousand_note(1)
                else:
                    five_hundred_note(1)
                    if (amount % 5000)%100 == 0:
                        one_hundred_note(((amount % 5000)-500)//100)
                    elif amount % 5000 < 600:
                        if (amount % 5000)-500 >= 50:
                            fifty_note(1)
                            if (amount % 5000) - 500 > 50:
                                ten_10 = (((amount % 5000) - 500)-50)//10
                                ten_note(ten_10)
                            else:
                                ten_10 = ((amount % 5000) - 500) // 10
                                ten_note(ten_10)

                                    #new
                    elif amount % 5000 > 600:
                        if (amount % 5000)%100 >= 50:
                            fifty_note(1)
                            if (amount % 5000)%100 > 50:
                                ten_10 = (((amount % 5000)%100)-50)//10
                                ten_note(ten_10)
                            else:
                                ten_10 = ((amount % 5000)%100) // 10
                                ten_note(ten_10)
            elif (amount % 5000) >1000:
                if (amount % 5000) % 1000==0:
                    one_thousand_note((amount % 5000) // 1000)
                else:
                    one_thousand_note((amount % 5000) // 1000)
                    if (amount % 5000) % 1000==500:
                        five_hundred_note(1)
                    elif (amount % 5000) % 1000>500:
                        five_hundred_note(1)
                        remainder_minus_500 = (amount % 5000) % 1000
                        if remainder_minus_500 < 600:
                            if remainder_minus_500>=50:
                                fifty_note(1)
                                if remainder_minus_500 > 50:
                                    ten_10 = (remainder_minus_500 -50)//10
                                    ten_note(ten_10)
                            else:
                                ten_10 = (remainder_minus_500) // 10
                        if remainder_minus_500 > 600:
                            if remainder_minus_500 % 100==0:
                                one_hundred_note((remainder_minus_500-500)//100)
                            else:
                                one_hundred_note((remainder_minus_500 - 500) // 100)
                                if remainder_minus_500 % 100>=50:
                                    fifty_note(1)
                                    if remainder_minus_500 % 100 >= 50:
                                        ten_10 = ((remainder_minus_500 % 100)-50)//10
                                        ten_note(ten_10)
                                    else:
                                        ten_10 = ((remainder_minus_500 % 100)) // 10
                                        ten_note(ten_10)

                        if remainder_minus_500 < 600:
                            if remainder_minus_500>=50:
                                fifty_note(1)
                                if remainder_minus_500 > 50:
                                    ten_10 = (remainder_minus_500 -50)//10
                                    ten_note(ten_10)
                            else:
                                ten_10 = (remainder_minus_500) // 10
                                ten_note(ten_10)
                    elif (amount%5000)%1000<500:
                        if ((amount%5000)%1000)%100==0:
                            one_hundred_note(((amount%5000)%1000)%100)
                        else:
                            if (amount%5000)%1000<100 or ((amount%5000)%1000)%100<100:
                                if (amount%5000)%1000>=50 or ((amount%5000)%1000)%100>=50:
                                    fifty_note(1)
                                    if (amount % 5000) % 1000 > 50:
                                        ten_note((((amount % 5000) % 1000)-50)//10)
                                    elif  ((amount % 5000) % 1000)%100 > 50:
                                        ten_note((((amount % 5000) % 1000) - 50) // 10)
                                else:
                                    if (amount % 5000)% 1000 < 50:
                                        ten_note(((amount % 5000) % 1000)//10)
                                    elif ((amount % 5000) % 1000) % 100 < 50:
                                        ten_note((((amount % 5000) % 1000)%100) // 10)



                            elif  ((amount%5000)%1000)>100:
                                if ((amount%5000)%1000)%100 ==0:
                                    one_hundred_note(((amount%5000)%1000)//100)







Pakistan_currency_denomination()


#if (amount < 1100 and amount > 1000) or (amount < 2100 and amount > 2000) or (amount < 3100 and amount > 3000) or(amount < 4100 and amount > 4000) or :