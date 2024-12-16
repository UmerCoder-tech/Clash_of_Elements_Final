import pygame

class UIManager:
    def __init__(self, screen, fonts, colors, draw_text):
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.draw_text = draw_text
        
        # Ressourcen zentral laden
        self.bg_image = pygame.image.load("Hintergrund/Fate's Moon.png")
        self.zuko_pb = pygame.image.load("Zuko/zuko_pb.png")
        self.susanoo_pb = pygame.image.load("Susanoo/susanoo_pb.png")

    def draw_bg(self):
        """Zeichnet den Hintergrund."""
        scaled_bg = pygame.transform.scale(self.bg_image, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(scaled_bg, (0, 0))


    def draw_health_bar(self, health, x, y):
        hb_width = 400
        hb_height = 30
        ratio = health / 100 
        pygame.draw.rect(self.screen, self.colors["BLACK"], (x - 2, y - 2, hb_width + 4, hb_height + 4))  # Rahmen
        pygame.draw.rect(self.screen, self.colors["WHITE"], (x, y, hb_width, hb_height))  # Hintergrund
        pygame.draw.rect(self.screen, self.colors["LILA"], (x, y, hb_width * ratio, hb_height))  # Lebensbalken

    def draw_mana_bar(self, mana, x, y):
        mb_width = 300
        mb_height = 20
        ratio = mana / 100
        pygame.draw.rect(self.screen, self.colors["BLACK"], (x - 2, y - 2, mb_width + 4, mb_height + 4))  # Rahmen
        pygame.draw.rect(self.screen, self.colors["WHITE"], (x, y, mb_width, mb_height))  # Hintergrund
        pygame.draw.rect(self.screen, self.colors["MIDNIGHT_BLUE"], (x, y, mb_width * ratio, mb_height))  # Manabalken

        if mana >= 100:
            self.draw_text(
                "Critical Attack Ready!", 
                self.fonts["ready_attack_font"], 
                self.colors["WHITE"], 
                x + mb_width // 2 - 50, 
                y + mb_height // 2 - 10
            )
    
    def draw_champion_profilepicture(self, player, x, y):
        """Zeichnet ein Profilbild basierend auf der Spieler-ID."""
        if player == 1:
            profile_image = self.zuko_pb  # Bild von Zuko
        elif player == 2:
            profile_image = self.susanoo_pb  # Bild von Susanoo
        
        frame_width, frame_height = 54, 54
        profile_width, profile_height = 50, 50
        pygame.draw.rect(self.screen, self.colors["BLACK"], (x - 2, y - 2, frame_width, frame_height))  # Rahmen
        profile_image = pygame.transform.scale(profile_image, (profile_width, profile_height))
        self.screen.blit(profile_image, (x, y))

    def draw_player_names(self, fighter_1_data, fighter_2_data):
        """
        Zeigt die Namen der Spieler unterhalb der Mana-Balken an.
        Die Namen werden dynamisch zentriert basierend auf ihrer Länge.
        """
        name_font = self.fonts["name_font"]

        # Berechnung der Breite der Namen
        name1_width = name_font.size(fighter_1_data["attributes"]["name"])[0]
        name2_width = name_font.size(fighter_2_data["attributes"]["name"])[0]

        # Dynamische Positionen für die Namen
        name1_x = 120 - name1_width // 2  # Zentriere unter Mana-Balken 1
        name2_x = 870 - name2_width // 2  # Zentriere unter Mana-Balken 2

        # Namen zeichnen
        self.draw_text(fighter_1_data["attributes"]["name"], name_font, self.colors["WHITE"], name1_x, 90)  # Y-Offset für 

    
