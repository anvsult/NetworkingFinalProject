from game_logic import *
import random


def random_bot(grid, bot_symbol, player_symbol):
    available_moves = []
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                available_moves.append((row, col))
    return random.choice(available_moves) if available_moves else None


def medium_bot(grid, bot_symbol, player_symbol):
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                grid[row][col] = bot_symbol
                if check_winner(grid) == bot_symbol:
                    return row, col
                grid[row][col] = None

    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                grid[row][col] = player_symbol
                if check_winner(grid) == player_symbol:
                    grid[row][col] = bot_symbol
                    return row, col
                grid[row][col] = None

    return random_bot(grid, bot_symbol, player_symbol)


def minimax(grid, depth, is_maximizing, bot_symbol, player_symbol):
    winner = check_winner(grid)
    if winner == bot_symbol:
        return 10 - depth
    elif winner == player_symbol:
        return depth - 10
    elif all(cell is not None for row in grid for cell in row):
        return 0  # Draw

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] is None:
                    grid[row][col] = bot_symbol
                    score = minimax(grid, depth + 1, False, bot_symbol, player_symbol)
                    grid[row][col] = None
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if grid[row][col] is None:
                    grid[row][col] = player_symbol
                    score = minimax(grid, depth + 1, True, bot_symbol, player_symbol)
                    grid[row][col] = None
                    best_score = min(best_score, score)
        return best_score


def hard_bot(grid, bot_symbol, player_symbol):
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if grid[row][col] is None:
                grid[row][col] = bot_symbol
                score = minimax(grid, 0, False, bot_symbol, player_symbol)
                grid[row][col] = None
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


