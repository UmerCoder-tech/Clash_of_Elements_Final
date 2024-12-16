import pygame
from pygame import mixer


# Initialisiere Pygame
pygame.init()
mixer.init()

main_theme = pygame.mixer.music.load("Audio/Ryus Ost.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

dragon_slayer_fx = pygame.mixer.Sound("Audio/assets_audio_magic.wav")
dragon_slayer_fx.set_volume(0.5)
katana__fx = pygame.mixer.Sound("Audio/assets_audio_sword.wav")
katana__fx.set_volume(0.5)

# Bildschirmgröße und Framerate
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

# Farben

colors = {
    "LILA": (128, 0, 128),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "MIDNIGHT_BLUE": (25, 25, 112), 
    "SILBER": (192, 192, 192),
    "GOLD": (255, 215, 0),
    "DUNKEL_GRÜN": (0, 100, 0),
    "RED": (255, 0, 0),
    "BLUE":(0, 0, 255)
}


#define fonts
fonts = {
    "count_font": pygame.font.Font("Fonts/Orbitron.ttf", 180),
    "score_font": pygame.font.Font("Fonts/Orbitron.ttf", 100),
    "ready_attack_font": pygame.font.Font("Fonts/Oswald.ttf", 16),
    "name_font": pygame.font.Font("Fonts/Oswald.ttf", 28),
    "fight_font": pygame.font.Font("Fonts/Oswald.ttf", 300),
    "berserk_front": pygame.font.Font("Fonts/MetalMania.ttf", 120),
    "winner_font": pygame.font.Font("Fonts/Oswald.ttf", 150),
}


def draw_text(text, font, text_colour, x, y):
    # text: Der anzuzeigende Text (String).
    # font: Das pygame.font.Font-Objekt, das den Schriftstil und die Größe definiert.
    # text_colour: Die Farbe des Textes als RGB-Tupel, z. B. (255, 255, 255) für Weiß.
    # x, y: Die Koordinaten, an denen der Text auf dem Bildschirm gezeichnet wird.

    img = font.render(text, True, text_colour)  # Render den Text als Bild (antialiasing=True, text_col für die Farbe).
    screen.blit(img, (x, y))  # Zeichne das Bild an die gewünschte Position auf dem Bildschirm.



# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Fighting Game")
clock = pygame.time.Clock()

# Jetzt die Spritesheets importieren
from spritesheets import animations_zuko, animations_susanoo
from champions import Fighter
from gamelogic import GameLogic
from ui_manager import UIManager



# Spieler erstellen
fighter_1 = Fighter(1, 200, 310, animations_zuko, dragon_slayer_fx)  # Spieler 1
fighter_2 = Fighter(2, 700, 310, animations_susanoo, katana__fx)  # Spieler 2

# Initialisierung der Spiel-Logik
game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)
ui_manager = UIManager(screen, fonts, colors, draw_text)


# Hauptspiel-Schleife
run = True
while run:
    clock.tick(FPS)     #clock.ticks recherchieren

    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ui_manager.draw_bg()
    ui_manager.draw_champion_profilepicture(1, 20, 64)  # Spieler 1 (Zuko)
    ui_manager.draw_champion_profilepicture(2, 930, 64)  # Spieler 2 (Susanoo)



    # Lebensbalken zeichnen
    ui_manager.draw_health_bar(fighter_1.health, 20, 20)
    ui_manager.draw_health_bar(fighter_2.health, 580, 20)
    


    #Manabalken
    ui_manager.draw_mana_bar(fighter_1.mana, 80, 65)
    ui_manager.draw_mana_bar(fighter_2.mana, 618, 65)

    #namen der spieler alt
    draw_text("ZUKO",fonts["name_font"], colors["RED"], 80, 80)
    draw_text("SUSANOO",fonts["name_font"], colors["BLUE"], 817, 80)

    #neu name
    # i_manager.draw_player_names(fighter_1_data, fighter_2_data)
    

    # Countdown aktualisieren
    game_logic.update_countdown()

    # Timer aktualisieren und anzeigen (startet erst nach Countdown)
    game_logic.update_timer()

    game_logic.check_berserker_phase()
    game_logic.update_fighter_berserker_state()

    # Berserker-Nachricht anzeigen
    game_logic.display_berserker_message()

    # Runde prüfen
    game_logic.check_round_status()

    # Rundengewinne zeichnen
    game_logic.draw_round_wins()

    # Spieler-Updates und Zeichnen
    if game_logic.intro_count <= 0:
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1)
        fighter_1.update()
        fighter_2.update()

            

    fighter_1.update()
    fighter_2.update()

    # Spieler zeichnen
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    game_logic.ermittle_winner()

    game_logic.update_timer()
           

    # Bildschirm aktualisieren
    pygame.display.update()