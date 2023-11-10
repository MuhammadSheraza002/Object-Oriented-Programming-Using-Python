import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.draw.circle(screen, 'green', (200, 200), 100, 2) # 2 is the width of norder
    pygame.display.update()

main()
