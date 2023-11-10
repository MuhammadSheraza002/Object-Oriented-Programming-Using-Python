from random import randint
def sum_digit_number(n):
    if n < 10:
        return n
    return n % 10 + sum_digit_number(n//10)
n = randint(1,100)
print(n)
print(sum_digit_number(n))