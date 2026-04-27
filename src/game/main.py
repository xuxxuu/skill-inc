import pygame
from pygame.typing import ColorLike, Point
from skills import SkillHandler


class Button(pygame.sprite.Sprite):
    def __init__(self, tag: str, pos: Point, color: ColorLike, size: Point):
        super().__init__()
        self.tag = tag
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.skill_handler = SkillHandler()
        self.wc_button = Button("woodcutting", (100, 100), (255, 0, 0), (100, 100))  # temp button
        self.fishing_button = Button("fishing", (100, 250), (0, 0, 255), (100, 100))  # temp button
        self.buttons = pygame.sprite.LayeredUpdates(self.wc_button, self.fishing_button)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # create iter here to then be able to call next() with a default
                    button_maybe = iter(self.buttons.get_sprites_at(event.pos))
                    # the rare walrus operator. tbh i just think this approach looked cleaner. No other reason.
                    if button := next(button_maybe, None):
                        self.skill_handler.execute_skill(button.tag)

            self.screen.fill((0, 0, 0))
            self.buttons.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
