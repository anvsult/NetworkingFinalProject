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
    warning_msg1 = "HAHA!"
    warning_msg2 = "Your files have been encrypted!"
    instruction_msg1 = "Win the game to decrypt them. Press any key to start."
    instruction_msg2 = "You have 3 attempts"

    while True:
        SCREEN.fill(WHITE)
        draw_text_centered(warning_msg1, MESSAGE_FONT, RED, -100)
        draw_text_centered(warning_msg2, MESSAGE_FONT, RED, -50)
        draw_text_centered(instruction_msg1, SMALL_FONT, BLACK, 20)
        draw_text_centered(instruction_msg2, SMALL_FONT, BLACK, 60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return # Exit the function and start the game


def show_when_user_won():
    warning_msg1 = "You won!"
    warning_msg2 = "Your files have been decrypted!"
    instruction_msg = "Press any key to close the game"

    while True:
        SCREEN.fill(WHITE)
        draw_text_centered(warning_msg1, MESSAGE_FONT, RED, -50)
        draw_text_centered(warning_msg2, MESSAGE_FONT, RED, 20)
        draw_text_centered(instruction_msg, SMALL_FONT, BLACK, 90)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                exit()


def show_when_bot_won():
    warning_msg1 = "You lost!"
    warning_msg2 = "Your files will remain encrypted FOREVER!"
    instruction_msg = "Press any key to close the game"

    while True:
        SCREEN.fill(WHITE)
        draw_text_centered(warning_msg1, MESSAGE_FONT, RED, -50)
        draw_text_centered(warning_msg2, MESSAGE_FONT, RED, 20)
        draw_text_centered(instruction_msg, SMALL_FONT, BLACK, 90)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                exit()


# Draw a button
def draw_button(text, font, color, button_rect, hover_color=None):
    pygame.draw.rect(SCREEN, color, button_rect)
    if hover_color:
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(SCREEN, hover_color, button_rect)

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    SCREEN.blit(text_surface, text_rect)


# Updated show_end_of_round
def show_end_of_round():
    warning_msg1 = "You lost this round!"
    button_text = "Next Round"
    button_width, button_height = 200, 60
    button_rect = pygame.Rect(
        (WIDTH - button_width) // 2, (HEIGHT + 50) // 2, button_width, button_height
    )

    while True:
        SCREEN.fill(WHITE)
        draw_text_centered(warning_msg1, MESSAGE_FONT, RED, -50)
        draw_button(button_text, SMALL_FONT, BLUE, button_rect, hover_color=DARK_BLUE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Exit the function and start the next round
