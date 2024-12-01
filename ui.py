
import pygame
import random
from constants import *

def draw_grid():
    SCREEN.fill(BACKGROUND_COLOR)  # Set background color

    for x in range(1, 3):
        # VERTICAL LINES
        pygame.draw.line(SCREEN, GRID_COLOR, (HORIZONTAL_OFFSET + x * CELL_SIZE, 0), (x * CELL_SIZE + HORIZONTAL_OFFSET, HEIGHT), LINE_WIDTH)
        # HORIZONTAL LINES
        pygame.draw.line(SCREEN, GRID_COLOR, (HORIZONTAL_OFFSET, x * CELL_SIZE), (WIDTH - HORIZONTAL_OFFSET, x * CELL_SIZE), LINE_WIDTH)

def draw_symbols():
    for row in range(3):
        for col in range(3):
            symbol = GRID[row][col]
            if symbol:
                text = FONT.render(symbol, True, SYMBOL_COLOR)
                SCREEN.blit(text, (HORIZONTAL_OFFSET + col * CELL_SIZE + CELL_SIZE // 3 + random.randint(-2, 2),
                                   row * CELL_SIZE + CELL_SIZE // 4 + random.randint(-2, 2)))

def draw_flickering_text(text, font, color, y_offset, flicker_rate=500):
    if pygame.time.get_ticks() % flicker_rate < flicker_rate // 2:
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
        SCREEN.blit(surface, rect)

def animate_grid():
    for _ in range(3):
        x = random.randint(1, 3) * CELL_SIZE
        y = random.randint(1, 3) * CELL_SIZE
        pygame.draw.line(SCREEN, GRID_COLOR, (x, 0), (x, HEIGHT), LINE_WIDTH)
        pygame.draw.line(SCREEN, GRID_COLOR, (0, y), (WIDTH, y), LINE_WIDTH)

def draw_title():
    title_font = pygame.font.Font(None, 64)  # Larger font for the title
    draw_flickering_text("System Locked!", title_font, TEXT_COLOR, -100)

