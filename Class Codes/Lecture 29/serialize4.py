from pickle import *
from random import *

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
        return super().__str__() + f'\tZ: {self.__z}'

class Points:
    def __init__(self, count):
        self.points = []
        for i in range(count):
            self.points.append(Point3D(randint(1,9), randint(1,9), randint(1,9)))
    def __str__(self):
        string = ''
        for point in self.points:
            string += str(point) + '\n'
        return string

p1 = Points(4)
file = open('points_points.bin', mode='wb')
dump(p1, file)
file.close()
print ('---------------')
file = open('points_points.bin', mode='rb')
p2 = load(file)
print(p2)
file.close()
