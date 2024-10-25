import pygame
from colors import Colors

class Block:
    def __init__(self, identifier):
        self.id = identifier
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0 #  possible value -> 0, 1, 2, 3
        self.colors = Colors.get_cell_colors()

    def draw(self, screen):
        tiles = self.cells[self.rotation_state]

        for tile in tiles:
            x = tile.column * self.cell_size + 1
            y = tile.row * self.cell_size + 1
            size = self.cell_size - 1

            tile_rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)