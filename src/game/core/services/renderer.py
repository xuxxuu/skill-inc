import pygame
from pygame import Surface

from core.player import Player


class Renderer:
    def __init__(self, screen: Surface, player: Player) -> None:
        self.screen = screen
        self.player = player
        self.font = pygame.font.SysFont("caskaydiacovenerdfont", 50, True)
        self.currency_text = self.font.render(f"{self.player.inventory.currency}", True, "black")
        self.currency_rect = self.currency_text.get_rect(center=(500, 500))

    def update_currency_render(self):
        self.currency_text = self.font.render(f"{self.player.inventory.currency}", True, "black")

    def render_ui(self):
        self.screen.blit(self.currency_text, self.currency_rect)

    def update(self):
        self.render_ui()
