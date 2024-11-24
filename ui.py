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
                text = SYMBOL_FONT.render(symbol, True, RED)
                SCREEN.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 4))


def draw_text_centered(text, font, color, y_offset):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    SCREEN.blit(surface, rect)


def show_warning():
    warning1_msg = "HAHA!"
    warning2_msg = "Your files have been encrypted!"
    instruction_msg = "Win the game to decrypt them. Press any key to start."

    while True:
        SCREEN.fill(WHITE)
        draw_text_centered(warning1_msg, MESSAGE_FONT, RED, -100)
        draw_text_centered(warning2_msg, MESSAGE_FONT, RED, -50)
        draw_text_centered(instruction_msg, SMALL_FONT, BLACK, 20)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return # Exit the function and start the game