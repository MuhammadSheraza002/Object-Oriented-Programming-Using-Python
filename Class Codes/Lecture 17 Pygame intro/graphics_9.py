import pygame
import time
import random as r

def main():
    screen = pygame.display.set_mode((600, 700))
    screen.fill('white')    #set white back ground
    #code to draw text on graphics screen
    pygame.init()  #init function required for some tasks, like setting font
    calibri = pygame.font.SysFont('Calibri', 48)
    text = calibri.render('M O V I N G', True, (50,125,250), 'white')
    text_rect = text.get_rect()
    text_rect.center = (300, 50)
    screen.blit(text, text_rect)
    #code to move circle on the screen
    for i in range(2):
        x = r.randint(100, 500)
        y = r.randint(200, 500)
        pygame.draw.circle(screen, (50,125,250), (x, y), 60)
        pygame.display.update()
        time.sleep(0.5)
        pygame.draw.circle(screen, (255,255,255), (x, y), 60)
        pygame.display.update()

main()

