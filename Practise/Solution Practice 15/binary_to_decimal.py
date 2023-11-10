def binary_to_decimal(x, p=0):
    if type(x) == str:    return binary_to_decimal(int(x))
    if x==0:   return 0
    return (x%2)*(2**p)+binary_to_decimal(int(x/10), p+1)


def main():
    print(binary_to_decimal('1011'))
    print(binary_to_decimal('1111'))
    print(binary_to_decimal('1001'))
    print(binary_to_decimal('111111'))
    print(binary_to_decimal('1100'))
    print(binary_to_decimal('1110'))
    print(binary_to_decimal('11101'))
    print(binary_to_decimal('11010'))

main()
