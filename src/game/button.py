import pygame
from pygame.typing import ColorLike, Point


class Button(pygame.sprite.Sprite):
    def __init__(self, tag: str, pos: Point, color: ColorLike, size: Point):
        super().__init__()
        self.tag = tag
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
