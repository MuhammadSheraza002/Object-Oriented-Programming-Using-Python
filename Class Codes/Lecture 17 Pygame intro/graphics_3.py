import pygame

def main():
    screen = pygame.display.set_mode((600, 600))
    pygame.draw.circle(screen, 'green', (200, 200), 100)
    pygame.display.update()

main()
