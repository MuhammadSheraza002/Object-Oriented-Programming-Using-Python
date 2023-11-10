import pygame

def main():
    screen = pygame.display.set_mode((600, 600))
    pygame.draw.line(screen, 'blue', (300, 300), (400, 300))
    pygame.draw.line(screen, 'cyan', (300, 300), (300, 200))
    pygame.draw.line(screen, 'gray', (300, 300), (380, 220))
    pygame.display.update()

main()
