from Circle import *
import pygame as py

class Shaded_Circle(Circle):
    def __init__(self,screen,x,y,radius,color):
        Circle.__init__(self,screen,x,y,radius,color)

    def draw(self):
        py.draw.circle(self.screen,self.color,self.__center_x,self.__center_y,sel)
