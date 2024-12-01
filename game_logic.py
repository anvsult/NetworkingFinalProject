from constants import *


# Check for a win
def check_winner(grid = GRID):
    # Rows, columns, and diagonals
    for row in GRID:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(len(GRID)):
        if GRID[0][col] == GRID[1][col] == GRID[2][col] and GRID[0][col] is not None:
            return GRID[0][col]
    if GRID[0][0] == GRID[1][1] == GRID[2][2] and GRID[0][0] is not None:
        return GRID[0][0]
    if GRID[0][2] == GRID[1][1] == GRID[2][0] and GRID[0][2] is not None:
        return GRID[0][2]
    return None


# Check for a draw
def is_draw():
    return all(cell is not None for row in GRID for cell in row)

def reset_board():
    global GRID, winner, game_over, player
    GRID = [[None for _ in range(3)] for _ in range(3)]  # Reset grid
    winner = None
    game_over = False
    player = "X"  # Start with player X again
