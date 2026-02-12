import pygame
import sys
import random

# Pygame başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 600, 700
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Renkler
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (52, 73, 94)
BUTTON_HOVER = (41, 128, 185)

# Ekran oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3 Taş Oyunu - Tic Tac Toe')

# Font
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)

# Oyun tahtası (3x3 matris)
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Oyuncu (X başlar)
player = 'X'
game_over = False
winner = None

def draw_lines():
    """Oyun tahtası çizgilerini çiz"""
    # Yatay çizgiler
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Dikey çizgiler
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, 600), LINE_WIDTH)

def draw_figures():
    """X ve O işaretlerini çiz"""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR,
                    (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                     int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                    CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                    CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    CROSS_WIDTH)

def mark_square(row, col, player_mark):
    """Kareye işaret koy"""
    board[row][col] = player_mark

def available_square(row, col):
    """Karenin boş olup olmadığını kontrol et"""
    return board[row][col] is None

def is_board_full():
    """Tahta dolu mu kontrol et"""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def get_empty_squares():
    """Boş kareleri bul"""
    empty = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                empty.append((row, col))
    return empty

def check_win_move(player_mark):
    """Kazanma hamlesi var mı kontrol et (tahta değiştirmeden)"""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                board[row][col] = player_mark
                win = False
                # Dikey
                for c in range(BOARD_COLS):
                    if board[0][c] == board[1][c] == board[2][c] == player_mark:
                        win = True
                # Yatay
                for r in range(BOARD_ROWS):
                    if board[r][0] == board[r][1] == board[r][2] == player_mark:
                        win = True
                # Çaprazlar
                if board[0][0] == board[1][1] == board[2][2] == player_mark:
                    win = True
                if board[0][2] == board[1][1] == board[2][0] == player_mark:
                    win = True
                board[row][col] = None
                if win:
                    return (row, col)
    return None

def computer_move():
    """Bilgisayar hamlesi - Akıllı AI"""
    # 1. Kazanabilecek hamle var mı?
    win_move = check_win_move('O')
    if win_move:
        return win_move

    # 2. Rakibin kazanmasını engelle
    block_move = check_win_move('X')
    if block_move:
        return block_move

    # 3. Merkezi al
    if board[1][1] is None:
        return (1, 1)

    # 4. Köşeleri al
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    empty_corners = [c for c in corners if board[c[0]][c[1]] is None]
    if empty_corners:
        return random.choice(empty_corners)

    # 5. Kalan boş karelerden birini seç
    empty = get_empty_squares()
    if empty:
        return random.choice(empty)

    return None

def check_win(player_mark):
    """Kazanan var mı kontrol et"""
    # Dikey kontrol
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player_mark:
            draw_vertical_winning_line(col, player_mark)
            return True

    # Yatay kontrol
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player_mark:
            draw_horizontal_winning_line(row, player_mark)
            return True

    # Çapraz kontrol (sol üst - sağ alt)
    if board[0][0] == board[1][1] == board[2][2] == player_mark:
        draw_asc_diagonal(player_mark)
        return True

    # Çapraz kontrol (sağ üst - sol alt)
    if board[0][2] == board[1][1] == board[2][0] == player_mark:
        draw_desc_diagonal(player_mark)
        return True

    return False

def draw_vertical_winning_line(col, player_mark):
    """Dikey kazanma çizgisi"""
    color = CIRCLE_COLOR if player_mark == 'O' else CROSS_COLOR
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, color, (posX, 15), (posX, 600 - 15), 15)

def draw_horizontal_winning_line(row, player_mark):
    """Yatay kazanma çizgisi"""
    color = CIRCLE_COLOR if player_mark == 'O' else CROSS_COLOR
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal(player_mark):
    """Çapraz kazanma çizgisi (sol üst - sağ alt)"""
    color = CIRCLE_COLOR if player_mark == 'O' else CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, 600 - 15), 15)

def draw_desc_diagonal(player_mark):
    """Çapraz kazanma çizgisi (sağ üst - sol alt)"""
    color = CIRCLE_COLOR if player_mark == 'O' else CROSS_COLOR
    pygame.draw.line(screen, color, (15, 600 - 15), (WIDTH - 15, 15), 15)

def draw_status():
    """Alt bilgi panelini çiz"""
    # Alt panel arkaplanı
    pygame.draw.rect(screen, (44, 62, 80), (0, 600, WIDTH, 100))

    if game_over:
        if winner == 'X':
            text = "Tebrikler! Kazandın! 🎉"
        elif winner == 'O':
            text = "Bilgisayar Kazandı! 🤖"
        else:
            text = "Berabere! 🤝"
    else:
        if player == 'X':
            text = "Senin Sıran (X)"
        else:
            text = "Bilgisayar düşünüyor..."

    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 630))
    screen.blit(text_surface, text_rect)

    # Yeniden başlat butonu
    restart_text = small_font.render("R tuşu: Yeniden Başlat", True, TEXT_COLOR)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, 670))
    screen.blit(restart_text, restart_rect)

def restart():
    """Oyunu sıfırla"""
    global board, player, game_over, winner
    screen.fill(BG_COLOR)
    draw_lines()
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 'X'
    game_over = False
    winner = None

# Oyun başlangıcı
screen.fill(BG_COLOR)
draw_lines()

# Ana oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x koordinatı
            mouseY = event.pos[1]  # y koordinatı

            # Sadece oyun tahtası alanında tıklamayı kabul et
            if mouseY < 600:
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    draw_figures()

                    if check_win(player):
                        game_over = True
                        winner = player
                    elif is_board_full():
                        game_over = True
                        winner = None
                    else:
                        player = 'O'
                        pygame.display.update()
                        pygame.time.wait(500)  # Bilgisayar düşünüyor efekti

                        # Bilgisayar oynuyor
                        move = computer_move()
                        if move:
                            mark_square(move[0], move[1], 'O')
                            draw_figures()

                            if check_win('O'):
                                game_over = True
                                winner = 'O'
                            elif is_board_full():
                                game_over = True
                                winner = None
                            else:
                                player = 'X'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    draw_status()
    pygame.display.update()

