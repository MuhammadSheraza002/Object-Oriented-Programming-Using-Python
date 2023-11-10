import pygame

def main():
    screen = pygame.display.set_mode((600, 600))
    pygame.draw.line(screen, 'blue', (50, 100), (350, 100))
    pygame.draw.line(screen, 'cyan', (50, 100), (50, 350))
    pygame.draw.line(screen, 'gray', (50, 100), (300, 300))
    pygame.display.update()

main()
