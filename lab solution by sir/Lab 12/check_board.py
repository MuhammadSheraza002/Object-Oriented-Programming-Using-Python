from shape import *
from constants import *

class Checker_Board(Shape):
    box_size = 20
    def __init__(self, screen, x, y, color1=(86, 165, 204), color2=(211, 230, 129), bgcolor=(255,255,255), fillcolor=(120,120,120)):
        super().__init__(screen, color1, bgcolor, fillcolor)
        self.__color1 = color1
        self.__color2 = color2
        self.__x = x
        self.__y = y

    def draw(self):
        for x in range (self.__x, self.__x + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
            for y in range (self.__y, self.__y + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
                py.draw.rect(self.screen, self.__color1, (x, y, Checker_Board.box_size, Checker_Board.box_size))
        for x in range (self.__x + Checker_Board.box_size, self.__x + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
            for y in range (self.__y, self.__y + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
                py.draw.rect(self.screen, self.__color2, (x, y, Checker_Board.box_size, Checker_Board.box_size))
        py.display.update()
        for x in range (self.__x, self.__x + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
            for y in range (self.__y + Checker_Board.box_size, self.__y + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
                py.draw.rect(self.screen, self.__color2, (x, y, Checker_Board.box_size, Checker_Board.box_size))
        for x in range (self.__x + Checker_Board.box_size, self.__x + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
            for y in range (self.__y + Checker_Board.box_size, self.__y + Checker_Board.box_size * 8, Checker_Board.box_size+Checker_Board.box_size):
                py.draw.rect(self.screen, self.__color1, (x, y, Checker_Board.box_size, Checker_Board.box_size))
        py.display.update()

    def erase(self):
        py.display.update()