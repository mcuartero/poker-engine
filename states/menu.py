import pygame

class Menu:
    def draw(self, screen):
        title = self.title_font.render("Poker", True, (255, 255, 255))
        screen.blit(title, title.get_rect(center=(screen.get_width() // 2, 140)))
        for el in self.ui:
            el.draw(screen)