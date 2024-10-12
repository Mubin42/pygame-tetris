import sys
import pygame
from colors import Colors


pygame.init()

screen_width, screen_height, fps = 300, 600, 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

# event loop
while True:
    for event in pygame.event.get():
        # close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(Colors.dark_blue)
    pygame.display.update()
    clock.tick(fps)
