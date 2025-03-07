import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_HEIGHT

class PowerUp:
    def __init__(self, image, type) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.x = SCREEN_HEIGHT + random.randint(800,1000)
        self.rect.y = random.randint(100, 150)
        self.width = self.image.get_width()

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image,self.rect)

