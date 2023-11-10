from Shape import *
import pygame as py
from time import *

class Line(Shape):
    def __init__(self, screen, x1, y1, x2, y2, color='BLUE',size=10):
        super().__init__(screen, color)
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__size = size

    def draw(self):
        py.draw.line(self.screen, self.color, (self.__x1, self.__y1), (self.__x2, self.__y2),self.__size)
        py.display.update()

    def move(self, x, y):
        py.draw.line(self.screen,self.color,x,y)
        py.display.update()

    def increase_size(self,size):
        self.draw()
        sleep(1)
        self.remove()
        sleep(1)
        size = self.__size + ((size * self.__size)/100)
        self.__size = int(size)
        self.draw()