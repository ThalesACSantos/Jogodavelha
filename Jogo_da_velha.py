import pygame

# Inicialização do Pygame
pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Dimensões da tela
WIDTH = 600
HEIGHT = 600
SIZE: int = WIDTH // 3  # Tamanho de cada célula do tabuleiro

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

# Função para desenhar o tabuleiro
def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK,(0, i * SIZE), (WIDTH, i * SIZE), 2)
        pygame.draw.line(screen, BLACK,(i * SIZE, HEIGHT), (i * SIZE, 0), 2)

# Função para desenhar uma peça (X ou O)
def draw_piece(row, col, player):
    x = col * SIZE + SIZE // 2
    y = row * SIZE + SIZE // 2
    radius = SIZE // 4
    if player == 'X':
        pygame.draw.line(screen, RED, (x - radius, y - radius), (x + radius, y + radius), 2)
        pygame.draw.line(screen, RED, (x - radius, y + radius), (x + radius, y - radius), 2)
    else:
        pygame.draw.circle(screen, GREEN, (x, y), radius, 2)

# Função para verificar se houve um vencedor
def check_win(player):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Função para verificar se houve empate
def check_tie():
    for row in board:
        if ' ' in row:
            return False
    return True

# Inicializa o tabuleiro
board = [[' ' for _ in range(3)] for _ in range(3)]
player = 'X'

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            col = event.pos[0] // SIZE
            row = event.pos[1] // SIZE
            if board[row][col] == ' ':
                board[row][col] = player
                if check_win(player):
                    print(f"O jogador {player} venceu!")
                    running = False
                elif check_tie():
                    print("Empate!")
                    running = False
                player = 'O' if player == 'X' else 'X'

    screen.fill(WHITE)
    draw_board()
    for i in range(3):
        for j in range(3):
            if board[i][j] != ' ':
                draw_piece(i, j, board[i][j])
    pygame.display.flip()

pygame.quit()
