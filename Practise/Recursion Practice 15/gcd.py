def gcd(x,y):
    if x < y:
        return gcd(y,x)
    if x%y==0:
        return y
    return gcd(y,x%y)

def main():
    print(gcd(6,9))

main()