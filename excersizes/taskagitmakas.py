import pygame
import sys
import random

# Pygame başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Taş Kağıt Makas Oyunu ✊📄✂️')

# Renkler
BG_COLOR = (44, 62, 80)
BUTTON_COLOR = (52, 152, 219)
BUTTON_HOVER = (41, 128, 185)
WIN_COLOR = (46, 204, 113)
LOSE_COLOR = (231, 76, 60)
DRAW_COLOR = (241, 196, 15)
TEXT_COLOR = (255, 255, 255)
PANEL_COLOR = (33, 47, 60)

# Fontlar
title_font = pygame.font.Font(None, 60)
font = pygame.font.Font(None, 45)
small_font = pygame.font.Font(None, 32)
emoji_font = pygame.font.Font(None, 100)

# Oyun değişkenleri
player_score = 0
computer_score = 0
player_choice = None
computer_choice = None
result = None
game_state = "choosing"  # choosing, result, game_over
final_winner = None
MAX_SCORE = 3  # İlk 3'ü alan kazanır

# Seçenekler
choices = ['Tas', 'Kagit', 'Makas']
emojis = {'Tas': 'O', 'Kagit': '[]', 'Makas': 'X'}

# Buton sınıfı
class Button:
    def __init__(self, x, y, width, height, text, emoji):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.emoji = emoji
        self.hovered = False

    def draw(self):
        color = BUTTON_HOVER if self.hovered else BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=15)
        pygame.draw.rect(screen, TEXT_COLOR, self.rect, 3, border_radius=15)

        # Emoji
        emoji_surface = emoji_font.render(self.emoji, True, TEXT_COLOR)
        emoji_rect = emoji_surface.get_rect(center=(self.rect.centerx, self.rect.centery - 15))
        screen.blit(emoji_surface, emoji_rect)

        # Text
        text_surface = small_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.centery + 45))
        screen.blit(text_surface, text_rect)

    def check_hover(self, pos):
        self.hovered = self.rect.collidepoint(pos)
        return self.hovered

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Butonları oluştur
buttons = [
    Button(80, 200, 150, 130, 'Tas', 'O'),
    Button(275, 200, 150, 130, 'Kagit', '[]'),
    Button(470, 200, 150, 130, 'Makas', 'X')
]

# Yeniden oyna butonu
replay_button = Button(275, 380, 150, 60, 'Tekrar Oyna', '🔄')
replay_button.emoji = ''  # Emoji'yi kaldır

def determine_winner(player, computer):
    """Kazananı belirle"""
    if player == computer:
        return "draw"
    elif (player == 'Tas' and computer == 'Makas') or \
         (player == 'Kagit' and computer == 'Tas') or \
         (player == 'Makas' and computer == 'Kagit'):
        return "win"
    else:
        return "lose"

def draw_game():
    """Oyunu çiz"""
    global game_state

    screen.fill(BG_COLOR)

    # Başlık
    title = title_font.render('Taş Kağıt Makas', True, TEXT_COLOR)
    title_rect = title.get_rect(center=(WIDTH // 2, 40))
    screen.blit(title, title_rect)

    # Skor paneli
    pygame.draw.rect(screen, PANEL_COLOR, (50, 80, 600, 50), border_radius=10)
    score_text = font.render(f'Sen: {player_score}  -  Bilgisayar: {computer_score}', True, TEXT_COLOR)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 105))
    screen.blit(score_text, score_rect)

    # Hedef skor bilgisi
    target_text = small_font.render(f'(İlk {MAX_SCORE} skoru yapan kazanır)', True, (149, 165, 166))
    target_rect = target_text.get_rect(center=(WIDTH // 2, 138))
    screen.blit(target_text, target_rect)

    # Kapat butonu (sağ üst köşe)
    close_rect = pygame.Rect(WIDTH - 50, 10, 40, 40)
    mouse_pos = pygame.mouse.get_pos()
    close_color = LOSE_COLOR if close_rect.collidepoint(mouse_pos) else (100, 100, 100)
    pygame.draw.rect(screen, close_color, close_rect, border_radius=8)
    close_text = font.render('X', True, TEXT_COLOR)
    close_text_rect = close_text.get_rect(center=close_rect.center)
    screen.blit(close_text, close_text_rect)

    if game_state == "choosing":
        # Seçim yazısı
        choose_text = font.render('Seçimini Yap!', True, TEXT_COLOR)
        choose_rect = choose_text.get_rect(center=(WIDTH // 2, 175))
        screen.blit(choose_text, choose_rect)

        # Butonları çiz
        for button in buttons:
            button.draw()

        # Alt bilgi
        info_text = small_font.render('Bir seçenek tıkla', True, (149, 165, 166))
        info_rect = info_text.get_rect(center=(WIDTH // 2, 380))
        screen.blit(info_text, info_rect)

    elif game_state == "result":
        # Seçimleri göster
        # Oyuncu seçimi
        pygame.draw.rect(screen, PANEL_COLOR, (80, 160, 200, 150), border_radius=15)
        player_label = small_font.render('Senin Seçimin', True, TEXT_COLOR)
        player_label_rect = player_label.get_rect(center=(180, 180))
        screen.blit(player_label, player_label_rect)

        player_emoji = emoji_font.render(emojis[player_choice], True, TEXT_COLOR)
        player_emoji_rect = player_emoji.get_rect(center=(180, 240))
        screen.blit(player_emoji, player_emoji_rect)

        player_text = font.render(player_choice, True, TEXT_COLOR)
        player_text_rect = player_text.get_rect(center=(180, 290))
        screen.blit(player_text, player_text_rect)

        # VS
        vs_text = title_font.render('VS', True, DRAW_COLOR)
        vs_rect = vs_text.get_rect(center=(WIDTH // 2, 235))
        screen.blit(vs_text, vs_rect)

        # Bilgisayar seçimi
        pygame.draw.rect(screen, PANEL_COLOR, (420, 160, 200, 150), border_radius=15)
        comp_label = small_font.render('Bilgisayar', True, TEXT_COLOR)
        comp_label_rect = comp_label.get_rect(center=(520, 180))
        screen.blit(comp_label, comp_label_rect)

        comp_emoji = emoji_font.render(emojis[computer_choice], True, TEXT_COLOR)
        comp_emoji_rect = comp_emoji.get_rect(center=(520, 240))
        screen.blit(comp_emoji, comp_emoji_rect)

        comp_text = font.render(computer_choice, True, TEXT_COLOR)
        comp_text_rect = comp_text.get_rect(center=(520, 290))
        screen.blit(comp_text, comp_text_rect)

        # Sonuç
        if result == "win":
            result_text = "Kazandin!"
            result_color = WIN_COLOR
        elif result == "lose":
            result_text = "Kaybettin!"
            result_color = LOSE_COLOR
        else:
            result_text = "Berabere!"
            result_color = DRAW_COLOR

        pygame.draw.rect(screen, result_color, (200, 320, 300, 50), border_radius=10)
        result_surface = font.render(result_text, True, TEXT_COLOR)
        result_rect = result_surface.get_rect(center=(WIDTH // 2, 345))
        screen.blit(result_surface, result_rect)

        # Devam et butonu
        pygame.draw.rect(screen, BUTTON_COLOR if not replay_button.hovered else BUTTON_HOVER,
                        (250, 390, 200, 50), border_radius=10)
        replay_text = font.render('Devam Et', True, TEXT_COLOR)
        replay_rect = replay_text.get_rect(center=(350, 415))
        screen.blit(replay_text, replay_rect)

        # R tuşu bilgisi
        r_text = small_font.render('veya R tuşuna bas', True, (149, 165, 166))
        r_rect = r_text.get_rect(center=(WIDTH // 2, 460))
        screen.blit(r_text, r_rect)

    elif game_state == "game_over":
        # Oyun bitti ekranı
        if final_winner == "player":
            winner_text = "TEBRIKLER!"
            winner_text2 = "Oyunu Kazandin!"
            bg_color = WIN_COLOR
        else:
            winner_text = "OYUN BITTI"
            winner_text2 = "Bilgisayar Kazandi!"
            bg_color = LOSE_COLOR

        # Büyük kutu
        pygame.draw.rect(screen, bg_color, (100, 180, 500, 200), border_radius=20)

        winner_surface = title_font.render(winner_text, True, TEXT_COLOR)
        winner_rect = winner_surface.get_rect(center=(WIDTH // 2, 230))
        screen.blit(winner_surface, winner_rect)

        winner_surface2 = font.render(winner_text2, True, TEXT_COLOR)
        winner_rect2 = winner_surface2.get_rect(center=(WIDTH // 2, 280))
        screen.blit(winner_surface2, winner_rect2)

        final_score = font.render(f'Final Skor: {player_score} - {computer_score}', True, TEXT_COLOR)
        final_score_rect = final_score.get_rect(center=(WIDTH // 2, 330))
        screen.blit(final_score, final_score_rect)

        # Yeniden başlat butonu
        pygame.draw.rect(screen, BUTTON_COLOR, (200, 410, 140, 50), border_radius=10)
        new_game_text = font.render('Yeni Oyun', True, TEXT_COLOR)
        new_game_rect = new_game_text.get_rect(center=(270, 435))
        screen.blit(new_game_text, new_game_rect)

        # Kapat butonu
        pygame.draw.rect(screen, LOSE_COLOR, (360, 410, 140, 50), border_radius=10)
        quit_text = font.render('Kapat', True, TEXT_COLOR)
        quit_rect = quit_text.get_rect(center=(430, 435))
        screen.blit(quit_text, quit_rect)

def reset_round():
    """Turu sıfırla (skor korunur)"""
    global player_choice, computer_choice, result, game_state
    player_choice = None
    computer_choice = None
    result = None
    game_state = "choosing"

def reset_game():
    """Oyunu tamamen sıfırla"""
    global player_score, computer_score, final_winner
    player_score = 0
    computer_score = 0
    final_winner = None
    reset_round()

# Ana oyun döngüsü
clock = pygame.time.Clock()

while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kapat butonu (sağ üst köşe) - her zaman aktif
            close_rect = pygame.Rect(WIDTH - 50, 10, 40, 40)
            if close_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

            if game_state == "choosing":
                for i, button in enumerate(buttons):
                    if button.is_clicked(mouse_pos):
                        player_choice = choices[i]
                        computer_choice = random.choice(choices)
                        result = determine_winner(player_choice, computer_choice)

                        if result == "win":
                            player_score += 1
                        elif result == "lose":
                            computer_score += 1

                        # Skor kontrolü - biri 3'e ulaştı mı?
                        if player_score >= MAX_SCORE:
                            final_winner = "player"
                            game_state = "game_over"
                        elif computer_score >= MAX_SCORE:
                            final_winner = "computer"
                            game_state = "game_over"
                        else:
                            game_state = "result"

            elif game_state == "result":
                # Devam et butonuna tıklama
                replay_rect = pygame.Rect(250, 390, 200, 50)
                if replay_rect.collidepoint(mouse_pos):
                    reset_round()

            elif game_state == "game_over":
                # Yeni oyun butonu
                new_game_rect = pygame.Rect(200, 410, 140, 50)
                if new_game_rect.collidepoint(mouse_pos):
                    reset_game()

                # Kapat butonu (game over ekranındaki)
                quit_rect = pygame.Rect(360, 410, 140, 50)
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if game_state == "result":
                    reset_round()
                elif game_state == "game_over":
                    reset_game()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Hover kontrolü
    if game_state == "choosing":
        for button in buttons:
            button.check_hover(mouse_pos)
    elif game_state == "result":
        replay_button.rect = pygame.Rect(250, 390, 200, 50)
        replay_button.hovered = replay_button.rect.collidepoint(mouse_pos)

    draw_game()
    pygame.display.update()
    clock.tick(60)

