def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if x % y == 0:
        return y
    return gcd (y, x%y)

def main():
    print (gcd(36, 48))
    print (gcd(48, 36))
    print (gcd(36, 24))
    print (gcd(48, 24))
    print (gcd(50, 75))
    print (gcd(1, 2))

main()
