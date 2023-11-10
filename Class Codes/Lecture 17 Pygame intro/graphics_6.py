import pygame
import time

def main():
    screen = pygame.display.set_mode((600, 600))
    for width in range(2,20,2):
        pygame.draw.circle(screen, 'green', (200, 200), 100, width)
        pygame.display.update()
        time.sleep(1)

main()
