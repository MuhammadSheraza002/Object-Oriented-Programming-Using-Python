class Point:
    def __init__(self, x, y):
        self.__x = x        #data members are private, being started with __
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y

    #private method created just to demonstrate that outside access is not possible
    def __show(self):
        print (f'X: {self.__x}, Y: {self.__y}')

    def display(self):
        self.__show()
