class Complex_Number:
    count = 0   #class level member to count objects
    def __init__(self, a, b):
        self.set(a, b)
        Complex_Number.count += 1  # another object create
    def set(self, a, b):
        self.__a = a
        self.__b = b
    def __str__(self):
        if self.__p < 0 and self.__q<0:
            return f'{-self.__p} + i{-self.__q}'
        if self.__q < 0 and self.__p>0:
            return f'- {self.__p} + {-self.__q}'
        return f'{self.__p} + i{self.__q}'

    def simplify(self,p,q):
        i = 2
        common_divisor = 2
        while i <= p and i <= q:
            if p%i=0 and q % i =0:
                common_divisor=i
            i+=1
        return Complex_Number(p/common_divisor,q/common_divisor)



    def __mul__(self, obj):
        a = self.__a * obj.__a - self.__b * obj.__b
        b = self.__a * obj.__b + self.__b * obj.__a
        new_obj = Complex_Number(a, b)
        return new_obj
    def __del__(self):
        Complex_Number.count -= 1  #object deleted
