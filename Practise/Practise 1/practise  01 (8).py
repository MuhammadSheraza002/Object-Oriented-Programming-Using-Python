def find_largest_number_in_list(list):
    largest_number = list[0]
    for index in range(1,len(list)):
        if largest_number < list[index]:
            largest_number = list[index]
    return largest_number

def find_second_largest_number_in_list(list):
    largest_number = find_largest_number_in_list(list)
    second_largest_number = 0
    for index in range(len(list)):
        if list[index] < largest_number and second_largest_number < list[index]:
            second_largest_number = list[index]
    return second_largest_number
def main():
    list = [1,67,78,4,5]
    print(find_second_largest_number_in_list(list))
    print(*list)
main()

if amount == 5000:
    five_thousand_note(1)
elif amount < 5000:
    if amount % 1000 == 0:
        one_thousand_note(amount // 1000)
    else:
        one_thousand_note(amount // 1000)
        if amount % 1000 < 100:
            if amount % 1000 == 50:
                fifty_note(1)
            elif amount % 1000 > 50:
                fifty_note(1)
                ten_note(((amount % 1000) - 50) // 10)
            else:
                ten_note(((amount % 1000 - 50)) // 10)
        elif amount % 1000 >= 500:
            five_hundred_note(1)
            if (amount % 1000) > 500:
                if (amount % 1000) % 100 == 0:
                    hundred_100 = (amount % 1000 - 500) // 100
                    one_hundred_note(hundred_100)
                elif amount % 1000 < 600:
                    if (amount % 1000) % 100 >= 50:
                        fifty_note(1)
                        if ((amount % 1000) % 100) > 50:
                            ten_note(((amount % 1000 % 100) - 50) // 10)
                    else:
                        ten_note((amount % 1000 % 100) // 10)

                else:
                    if (amount % 1000) % 100 >= 50:
                        fifty_note(1)
                        if (amount % 1000) % 100 > 50:
                            ten_note(((amount % 1000) % 100 - 50) // 10)
                    else:
                        ten_note(((amount % 1000) % 100 - 50) // 10)
        elif amount % 1000 < 500 and amount % 1000 >= 100:
            if (amount % 1000) % 100 == 0:
                one_hundred_note((amount % 1000) // 100)
            else:
                if (amount % 1000) > 100:
                    one_hundred_note((amount % 1000) // 100)
                    if

                if (amount % 1000) >= 50 and (amount % 1000) < 100:
                    fifty_note(1)
                    if (amount % 1000) % 100 > 50:
                        ten_10 = ((amount % 1000) % 100 - 50) // 10
                        ten_note(ten_10)

                else:
                    ten_10 = ((amount % 1000) % 100) // 10
                    ten_note(ten_10)
