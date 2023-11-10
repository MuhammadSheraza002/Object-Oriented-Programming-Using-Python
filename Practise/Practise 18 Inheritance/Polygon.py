from Shape import *
from Line import *
from time import sleep
import pygame as py
class Polygon(Shape):
    def __init__(self,screen,x,y):
        Shape.__init__(self,screen)
        self.__x = x
        self.__y = y

    def draw(self):
        for i in range(len(self.__x)-1):
            py.draw.line(self.screen,self.color,(self.__x[i],self.__y[i]),(self.__x[i+1],self.__y[i+1]))
            py.display.update()
            sleep(1)
        py.draw.line(self.screen,self.color,(self.__x[-1], self.__y[-1]), (self.__x[0], self.__y[0]))
        py.display.update()
        sleep(1)







