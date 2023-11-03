import pygame
import sys

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 3
LINE_WIDTH = 6
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
O_COLOR = (255, 0, 0)
X_COLOR = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Game state
board = [['' for _ in range(3)] for _ in range(3)]
player_turn = 'X'
game_over = False
winner = None
game_started = False  # Track if the game has started

# Draw the grid
def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE), LINE_WIDTH)

# Draw the X and O symbols
def draw_symbols():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                x = col * CELL_SIZE + CELL_SIZE // 2
                y = row * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.line(screen, X_COLOR, (x - 40, y - 40), (x + 40, y + 40), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, (x + 40, y - 40), (x - 40, y + 40), LINE_WIDTH)
            elif board[row][col] == 'O':
                x = col * CELL_SIZE + CELL_SIZE // 2
                y = row * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.circle(screen, O_COLOR, (x, y), 40, LINE_WIDTH)

# Check for a win
def check_win(player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if not game_started:
                # Handle "Start" button click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if 100 <= x <= 200 and 200 <= y <= 250:
                        game_started = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    col, row = x // CELL_SIZE, y // CELL_SIZE
                    if board[row][col] == '':
                        board[row][col] = player_turn
                        if check_win(player_turn):
                            game_over = True
                            winner = player_turn
                        elif all(board[i][j] != '' for i in range(3) for j in range(3)):
                            game_over = True
                        else:
                            player_turn = 'X' if player_turn == 'O' else 'O'

    screen.fill(WHITE)
    if not game_started:
        # Draw the "Start" button
        pygame.draw.rect(screen, (0, 128, 0), (100, 200, 100, 50))
        font = pygame.font.Font(None, 36)
        start_text = font.render("Start", True, (255, 255, 255))
        screen.blit(start_text, (120, 210))
    else:
        draw_grid()
        draw_symbols()

    if game_over:
        font = pygame.font.Font(None, 36)
        if winner:
            text = f"Player {winner} wins!"
        else:
            text = "It's a draw!"
        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (50, 50))

    pygame.display.flip()

    if game_over:
        pygame.time.wait(3000)  # Pause for 3 seconds after the game ends
        pygame.quit()
        sys.exit()