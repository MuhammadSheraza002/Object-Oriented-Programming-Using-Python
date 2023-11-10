import pygame

def main():
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                break
        screen = pygame.display.set_mode((600, 600))
        pygame.draw.line(screen, 'blue', (0, 0), (600, 600))
        pygame.draw.line(screen, 'blue', (600, 0), (0, 600))
        pygame.draw.circle(screen, 'green', (300, 120), 60)
        pygame.draw.circle(screen, 'gray', (120, 300), 60)
        pygame.draw.circle(screen, 'red', (300, 480), 60)
        pygame.draw.circle(screen, 'cyan', (480, 300), 60)
        pygame.display.update()

main()
