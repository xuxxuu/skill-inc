import pygame
from skills import SkillHandler
from hpbars import TreeHPBar
from button import Button


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.skill_handler = SkillHandler()
        self.wc_button = Button("woodcutting", (100, 100), (255, 0, 0), (100, 100))  # temp button
        self.fishing_button = Button("fishing", (100, 250), (0, 0, 255), (100, 100))  # temp button
        self.buttons = pygame.sprite.LayeredUpdates(self.wc_button, self.fishing_button)
        self.tree_hp_bar = TreeHPBar((250, 100), (0, 255, 0), (200, 20))  # temp hp bar
        self.all_sprites = pygame.sprite.Group(self.wc_button, self.fishing_button, self.tree_hp_bar, self.tree_hp_bar)

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
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
