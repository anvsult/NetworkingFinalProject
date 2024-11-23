import pygame

pygame.init() # Necessary to load the fonts

# Screen dimensions and setup
WIDTH, HEIGHT = 900, 900
LINE_WIDTH = 5
CELL_SIZE = WIDTH // 3
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Grid setup
GRID = [[None for _ in range(3)] for _ in range(3)]

# Font
FONT = pygame.font.Font(None, 200)
MESSAGE_FONT = pygame.font.Font(None, 250)