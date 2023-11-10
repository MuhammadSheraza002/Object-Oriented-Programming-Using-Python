class Rational:
    def __init__(self):
        self.__p = 0
        self.__q = 1

    def set(self, p, q):
        self.__p = p
        if q == 0:
            q = 1
        self.__q = q

    def __str__(self):
        return f'{str(self.__p)}/{str(self.__q)}'

    def __eq__(self, obj):
        return self.__p == obj.__p and self.__q == obj.__q

    def __sub__(self, obj):
        new_object = Rational()
        new_object.__q = self.__q * obj.__q
        new_object.__p = (self.__p * obj.__q) - (self.__q * obj.__p)
        return new_object

def main():
    r1 = Rational()
    r2 = Rational()
    r3 = Rational()
    r1.set(2,5)
    r2.set(2,5)
    r3.set(3,1)
    print(r1)
    if r1 == r2:
        print ('Both are equal')
    if r1 == r3:
        print ('Both are equal')
    else:
        print ('Both are different')
    r4 = r1 - r3
    print(r4)

main()
