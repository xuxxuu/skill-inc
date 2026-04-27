from typing import Protocol
from pygame import Rect, sprite, Surface, SRCALPHA
from pygame.typing import ColorLike, Point

from core.inventory import Inventory

BUTTON_CONFIGS = [
    ("wood", (100, 100), "red"),
    ("wood", (100, 210), "yellow"),
    ("stone", (100, 320), "green"),
    ("stone", (100, 430), "purple"),
]


class Button(Protocol):
    tag: str
    pos: Point
    color: ColorLike
    image: Surface
    rect: Rect

    def click(self, inventory: Inventory): ...


class BuyButton(sprite.Sprite):
    """"""

    def __init__(self, tag: str, pos: Point, color):
        super().__init__()
        self.tag = tag
        self.pos = pos
        self.color = color
        self.image = Surface((100, 100), SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=self.pos)

    def click(self, inventory: Inventory):
        if inventory.currency >= inventory.item_costs[self.tag]:
            inventory.currency -= inventory.item_costs[self.tag]

    @staticmethod
    def generate_ui_buttons() -> list[Button]:
        buttons: list[Button] = [BuyButton(tag, pos, color) for tag, pos, color in BUTTON_CONFIGS]
        return buttons
