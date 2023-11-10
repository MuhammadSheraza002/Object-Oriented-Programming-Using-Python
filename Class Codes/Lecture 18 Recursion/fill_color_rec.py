import time
import random as r
import pygame as pg

#Re
def fill_shape(screen, x, y, fill_color, boundary_color):
    pixel_color = screen.get_at((x, y))[:3]
    if pixel_color == fill_color or pixel_color == boundary_color:   return
    screen.set_at((x, y), fill_color)
    pg.display.update()
    time.sleep(0.01)        #you can decrease/ increase time to make it faster or slower
    fill_shape(screen, x+1, y, fill_color, boundary_color)
    fill_shape(screen, x-1, y, fill_color, boundary_color)
    fill_shape(screen, x, y+1, fill_color, boundary_color)
    fill_shape(screen, x, y-1, fill_color, boundary_color)

def draw_shape(screen, clr, n):
    pg.draw.line(screen, clr, (200, 200), (200+int(20*n),200-int(20*n)))
    pg.draw.line(screen, clr, (200+int(30*n), 200+int(20*n)), (200+int(20*n),200-int(20*n)))
    pg.draw.line(screen, clr, (200+int(30*n), 200+int(20*n)), (200+int(10*n),200+int(30*n)))
    pg.draw.line(screen, clr, (200+int(15*n), 200+int(10*n)), (200+int(10*n),200+int(30*n)))
    pg.draw.line(screen, clr, (200+int(15*n), 200+int(10*n)), (200,200))
    pg.display.update()

def main():
    screen = pg.display.set_mode((800, 600))
    screen.fill('white')
    clr = (0,0,255)
    fill_color = (0,255,0)
    scale = 1.5
    draw_shape(screen, clr, scale)
    fill_shape(screen, 205, 200, fill_color, clr)
    pg.display.update()

main()

