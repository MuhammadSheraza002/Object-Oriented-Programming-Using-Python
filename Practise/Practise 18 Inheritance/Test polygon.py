from Polygon import *
from time import *
import pygame as py

def main():
    screen = py.display.set_mode((800, 600))
    screen.fill('white')
    py.display.update()
    p = Polygon(screen,[0,200,400,600,400,200,0],[200,400,400,200,100,100,200])
    p.draw()

main()