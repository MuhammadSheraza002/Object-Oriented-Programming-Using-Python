class Complex_Number:
    count = 0   #class level member to count objects
    def __init__(self, a, b):
        self.set(a, b)
        Complex_Number.count += 1  # another object create
    def set(self, a, b):
        self.__a = a
        self.__b = b
    def __str__(self):
        s=f'{self.__a}'
        if self.__b<0:
            return s+f'-i{-self.__b}'
        return s+f'+i{self.__b}'
    def __mul__(self, obj):
        a = self.__a * obj.__a - self.__b * obj.__b
        b = self.__a * obj.__b + self.__b * obj.__a
        new_obj = Complex_Number(a, b)
        return new_obj
    def __del__(self):
        Complex_Number.count -= 1  #object deleted
