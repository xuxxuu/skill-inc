import pygame
from core.sprites.button import BuyButton
from core.player import Player
from core.services.renderer import Renderer

TICK_EVENT = pygame.event.custom_type()


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.renderer = Renderer(self.screen, self.player)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.all_sprites.add(BuyButton.generate_ui_buttons())
        self.time_between_ticks = 1000
        pygame.time.set_timer(TICK_EVENT, self.time_between_ticks)

    def upgrade_tick_speed(self, upgrade_ratio: float) -> None:
        self.time_between_ticks = int(self.time_between_ticks * upgrade_ratio)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_maybe = iter(self.all_sprites.get_sprites_at(event.pos))
                    if button := next(button_maybe, None):  # the one time i will use walrus operator
                        button.click(self.player.inventory)
                        self.renderer.update_currency_render()
                        self.upgrade_tick_speed(0.8)
                        pygame.time.set_timer(TICK_EVENT, self.time_between_ticks)
                if event.type == TICK_EVENT:
                    print(f"One tick has passed: {self.time_between_ticks}")

            self.screen.fill("blue")
            self.all_sprites.draw(self.screen)
            self.renderer.update()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
