# slo hacks 2019 game design
# tonytheonlypony and rjmacaranas

import sys
import pygame

def run_game():
    # screen initialization
    top = 50
    left = 50
    white = (230, 230, 230)
    black = (0, 0, 0)
    red = (255, 0 , 0)
    titleCoord = (200, 20)

    pygame.init()
    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Minsweeper")

    screen.fill(black)
    textSurface = myFont.render('Minesweeper', False, white)
    screen.blit(textSurface, titleCoord)

    for i in range(9):
        for i in range(9):
            pygame.draw.rect(screen, white, [left + 60 * i, top, 60, 60], 2)
        top += 60

    # main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()




run_game()
