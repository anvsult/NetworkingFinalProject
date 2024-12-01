
from constants import *
import random


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
                text = SYMBOL_FONT.render(symbol, True, SYMBOL_COLOR)
                SCREEN.blit(text, (HORIZONTAL_OFFSET + col * CELL_SIZE + CELL_SIZE // 3 + random.randint(-2, 2),
                                   row * CELL_SIZE + CELL_SIZE // 4 + random.randint(-2, 2)))


def draw_flickering_text(text, font, color, y_offset, flicker_rate=500):
    if pygame.time.get_ticks() % flicker_rate < flicker_rate // 2:
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
        SCREEN.blit(surface, rect)


def draw_title():
    title_font = pygame.font.Font(None, 64)  # Larger font for the title
    draw_flickering_text("System Locked!", title_font, TEXT_COLOR, -100)


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
def show_end_of_round(games_counter):
    warning_msg1 = "You didn't win this one! You have {} attempts left".format(3 - games_counter)
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

                    return
            if event.type == pygame.MOUSEMOTION:
                if button_rect.collidepoint(event.pos):
                    draw_button(button_text, SMALL_FONT, DARK_BLUE, button_rect, hover_color=BLUE)


def show_game_over():
    warning_msg1 = "Game Over!"
    warning_msg2 = "You have no more attempts!"
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