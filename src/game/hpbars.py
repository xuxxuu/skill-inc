import pygame
from pygame.typing import ColorLike, Point


class TreeHPBar(pygame.sprite.Sprite):
    def __init__(self, pos: Point, color: ColorLike, size: Point):
        super().__init__()
        self.color = color
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        pygame.draw.rect(self.image, (0, 255, 0), self.image.get_rect(), width=4)  # pyright: ignore
        self.current_hp_surf = pygame.Surface(size)
        self.current_hp_rect = pygame.FRect(0, 0, *size)  # pyright: ignore

    def damage_tree(self, damage: int) -> None:
        self.current_hp_surf.fill((0, 0, 0, 0))
        self.current_hp_rect.width -= damage  # pyright: ignore
        self.current_hp_surf.fill((0, 255, 0))  # pyright: ignore
        self.image.blit(self.current_hp_surf, (0, 0), self.current_hp_rect)  # pyright: ignore
