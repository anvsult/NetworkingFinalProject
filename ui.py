import pygame
from constants import *


# Draw the grid
def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(SCREEN, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(SCREEN, BLACK, (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE), LINE_WIDTH)


# Draw symbols
def draw_symbols():
    for row in range(3):
        for col in range(3):
            symbol = GRID[row][col]
            if symbol:
                text = FONT.render(symbol, True, RED)
                SCREEN.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 4))


def draw_text_centered(text, font, color, y_offset):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    SCREEN.blit(surface, rect)