from random import randint
import pygame
import time

def circle_motion():
    screen = pygame.display.set_mode((600,600))
    screen.fill('black')
    colors = ['red','green','blue','white','pink','gray']
    i = 0
    while i < 20:
        x = randint(100, 500)
        y = randint(100, 500)
        pygame.draw.circle(screen,colors[randint(0,len(colors)-1)],(x,y),randint(50,100))
        pygame.display.update()
        screen.fill('black')
        time.sleep(0.25)
        i+=1

circle_motion()
