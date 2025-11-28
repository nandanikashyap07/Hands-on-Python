import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 300, 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("XO Game - Lavender Theme")


LAVENDER = (230, 230, 250)
BLACK = (0, 0, 0)


board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
font = pygame.font.SysFont("Arial", 60, bold=True)

def draw_board():
    SCREEN.fill(LAVENDER)

    
    pygame.draw.line(SCREEN, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(SCREEN, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(SCREEN, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(SCREEN, BLACK, (0, 200), (300, 200), 3)

   
    for r in range(3):
        for c in range(3):
            if board[r][c] != "":
                text = font.render(board[r][c], True, BLACK)
                SCREEN.blit(text, (c * 100 + 30, r * 100 + 20))

def check_winner():
    
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "":
            return True

    
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            return True

    if board[0][0] == board[1][1] == board[2][2] != "":
        return True

    if board[0][2] == board[1][1] == board[2][0] != "":
        return True

    return False

def check_draw():
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                return False
    return True

def restart():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 100
            col = x // 100

            if board[row][col] == "":
                board[row][col] = current_player

                if check_winner():
                    print(f"Player {current_player} wins!")
                    pygame.time.delay(1500)
                    restart()

                elif check_draw():
                    print("It's a draw!")
                    pygame.time.delay(1500)
                    restart()

                else:
                    current_player = "O" if current_player == "X" else "X"

    draw_board()
    pygame.display.update()
