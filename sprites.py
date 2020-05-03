import pygame
import random
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_players
        super().__init__(self.groups)
        self.game = game
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        pos_x = random.randint(1, WIDTH - 30)
        pos_y = random.randint(1, HEIGHT - 30)
        self.rect.center = (pos_x, pos_y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.left = max(0, self.rect.left - SPEED)
        elif keys[pygame.K_RIGHT]:
            self.rect.right = min(WIDTH, self.rect.right + SPEED)
        elif keys[pygame.K_UP]:
            self.rect.top = max(0, self.rect.top - SPEED)
        elif keys[pygame.K_DOWN]:
            self.rect.bottom = min(HEIGHT, self.rect.bottom + SPEED)
