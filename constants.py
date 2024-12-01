import pygame

pygame.init() # Necessary to load the fonts

# Screen dimensions and setup
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
HORIZONTAL_OFFSET = (WIDTH - HEIGHT) // 2  # Center the grid
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

LINE_WIDTH = 5
CELL_SIZE = HEIGHT // 3
# Fullscreen setup
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)  # Black background
GRID_COLOR = (139, 0, 0)  # Dark red for grid lines
SYMBOL_COLOR = (255, 0, 0)  # Bright red for symbols
TEXT_COLOR = (0, 255, 0)  # Neon green for text


# Grid setup
GRID = [[None for _ in range(3)] for _ in range(3)]

# Font
FONT = pygame.font.Font(None, 200)
MESSAGE_FONT = pygame.font.Font(None, 250)