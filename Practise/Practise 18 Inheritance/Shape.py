
import pygame as py

class Shape:
    def __init__(self,screen,color='blue',bgcolor = 'White'):
        self.screen = screen
        self.color = color
        self.bgcolor = bgcolor

    def draw(self):
        pass

    def move(self,x,y):
        pass

    def remove(self):
        self.screen.fill(self.bgcolor)
        py.display.update()

    def increase_size(self,size):
        pass

