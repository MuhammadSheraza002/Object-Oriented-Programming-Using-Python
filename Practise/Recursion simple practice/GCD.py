def GCD(x,y,gcd,i=1):
    if i>x or i > y:
        return gcd
    if x%i==0 and y%i==0:
        gcd = i
    return GCD(x,y,gcd,i+1)

from random import randint
def main():
    x = randint(1,100)
    y = randint(1,100)
    print(x)
    print(y)
    print(GCD(x,y,0))

main()