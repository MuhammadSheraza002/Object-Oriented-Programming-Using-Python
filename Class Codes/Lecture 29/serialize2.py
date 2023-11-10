from pickle import *

class Point2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'X: {self.__x}, Y: {self.__y}'

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z
    def __str__(self):
        return super().__str__() + f'\tZ: {self.__z}\n'

p1 = Point2D(1, 2)
p2 = Point3D(4, 5, 6)
file = open('points.bin', mode='wb+')
dump(p1,file)
dump(p2, file)
file.close()
file = open('points.bin', mode='rb')
#print(load(file))
print(load(file))
