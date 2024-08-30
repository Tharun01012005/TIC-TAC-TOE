import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500,500
LINE_WIDTH = 7  
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

WHITE = (255, 255, 255)
LINE_COLOR = (255, 255, 255)  
PLAYER_X_COLOR = (255, 0, 0)
PLAYER_O_COLOR = (0, 0, 255)

board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = 'X'
game_over = False
winner = None

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XO game")

def draw_grid():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

def draw_symbol(row, col):
    x_center = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y_center = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if board[row][col] == 'X':
        pygame.draw.line(screen, PLAYER_X_COLOR, (x_center - 42, y_center - 42), (x_center + 42, y_center + 42), 3)
        pygame.draw.line(screen, PLAYER_X_COLOR, (x_center + 42, y_center - 42), (x_center - 42, y_center + 42), 3)
    elif board[row][col] == 'O':
        pygame.draw.circle(screen, PLAYER_O_COLOR, (x_center, y_center), 40, 3)

def check_winner():

    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        elif all(cell == 'O' for cell in row):
            return 'O'

    for col in range(BOARD_SIZE):
        if all(row[col] == 'X' for row in board):
            return 'X'
        elif all(row[col] == 'O' for row in board):
            return 'O'

    if all(board[i][i] == 'X' for i in range(BOARD_SIZE)):
        return 'X'
    elif all(board[i][BOARD_SIZE - 1 - i] == 'X' for i in range(BOARD_SIZE)):
        return 'X'

    if all(board[i][i] == 'O' for i in range(BOARD_SIZE)):
        return 'O'
    elif all(board[i][BOARD_SIZE - 1 - i] == 'O' for i in range(BOARD_SIZE)):
        return 'O'

    return None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = current_player
                draw_symbol(clicked_row, clicked_col)

                winner = check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    game_over = True
                elif all(cell != '' for row in board for cell in row):
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    draw_grid()

    pygame.display.flip()

pygame.quit()
