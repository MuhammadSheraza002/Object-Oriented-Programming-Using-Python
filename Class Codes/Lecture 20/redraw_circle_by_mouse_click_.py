import pygame

def main():
    screen = pygame.display.set_mode((800, 600))
    screen.fill('white')
    pygame.display.update()
    last_x=-1
    last_y=-1
    while (True):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if last_x != -1:
                    pygame.draw.circle(screen, 'white', (last_x, last_y), 20)
                    pygame.draw.circle(screen, 'blue', (pos[0], pos[1]), 20)
                    pygame.display.update()
                    last_x, last_y = pos
                else:
                    pygame.draw.circle(screen, 'blue', (pos[0], pos[1]), 20)
                    pygame.display.update()
                    last_x, last_y = pos

main()
