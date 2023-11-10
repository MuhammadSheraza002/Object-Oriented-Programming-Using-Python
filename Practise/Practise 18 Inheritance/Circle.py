from time import *
from Shape import *
import pygame as py

class Circle(Shape):
    def __init__(self, screen, center_x, center_y, radius=100, color='BLUE'):
        super().__init__(screen, color)
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius


    def draw(self):
        py.draw.circle(self.screen, self.color, (self.__center_x, self.__center_y), self.__radius)
        py.display.update()

    def move(self, x, y):
        self.__center_x = x
        self.__center_y = y
        self.draw()

    def increase_size(self,size):
        self.draw()
        sleep(1)
        self.remove()
        sleep(1)
        size = self.__radius + ((size * self.__radius)/100)
        self.__radius = size
        self.draw()

    def set_color(self,color):
        self.color = color

    def set_center(self, x,y):
        self.__center_x = x
        self.__center_y = y

    def set_radius(self,radius):
        self.__radius = radius

    def get_color(self):
        return self.color

    def get_x_y(self):
        return self.__center_x,self.__center_y

    def get_radius(self):
        return self.__radius
