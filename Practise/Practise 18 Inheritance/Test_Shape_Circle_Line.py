import pygame as py
from Circle import *
from Line import *
from time import *

def main():
    screen = py.display.set_mode((800, 600))
    screen.fill('white')
    py.display.update()
    line = Line(screen, 100, 100, 200, 200)
    line.draw()
    sleep(1)
    line.remove()
    sleep(1)
    line.draw()
    sleep(1)
    line.remove()
    sleep(1)
    line.move((300,300), (600,600))
    sleep(1)
    line.remove()
    sleep(1)
    line.increase_size(100)
    sleep(1)
    line.remove()

    py.display.update()
    # line = Line(screen, 100, 100, 200, 200)
    circle = Circle(screen, 450, 250, 50)
    circle.draw()
    sleep(1)
    circle.remove()
    sleep(1)
    circle.draw()
    sleep(1)
    circle.move(250, 150)
    sleep(1)
    circle.increase_size(30)

main()
