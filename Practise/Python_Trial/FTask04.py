'''def check_number(n):
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count % 2 == 0:
        print(n, "is Crunchy")
    else:
        print(n, "is Ok but not Crunchy")

def main():
    n = int(input())
    check_number(n)

main()'''


def count_number(number):
    count = 0
    for index in range(1,number):
        if number % index==0:
            count+=1
    return count


def main():
    number = int(input("Enter positive integer: "))
    n = count_number(number)
    if n % 2 == 0:
        print(n,'Number is crunchy')
    if n % 2 != 0:
        print(n,'is ok, but not crunchy')

main()