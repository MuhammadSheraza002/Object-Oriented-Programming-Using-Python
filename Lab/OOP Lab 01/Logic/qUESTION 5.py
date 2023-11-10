'''
For this problem, we'll round an int value up to the next multiple of 10 if its
 rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to
the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds
down to 10. Given 3 ints, a b c, return the sum of their rounded values.
To avoid code repetition, write a separate helper "def round10(num):" and call
it 3 times. Write the helper entirely below and at the same indent level as
round_sum().

'''

def return_round(number):
    if number <=10:
        if 10 - number >5:
            return 0
        return 10
    str_num = str(number)
    int_num = int(str_num[0])
    if number-int_num*10> (int_num+1)*10-number:
        return (int_num+1)*10
    return int_num*10

def round_sum(a, b, c):
    return return_round(a) +return_round(b) + return_round(c)
print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))