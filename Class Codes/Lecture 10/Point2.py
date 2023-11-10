class Point:
    def __init__(self, x, y):
        self.set(x,y)

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def show(self):
        print (f'X: {self.__x}, Y: {self.__y}')
