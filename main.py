# Generate sprites and control one randomly chosen
import pygame
import random
from settings import *
from sprites import *


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.sprite_in_control = None
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        self.all_players = pygame.sprite.Group()
        for pl in range(SPRITES_QTT):
            Player(self)
        self.change_sprite_control()
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         self.change_sprite_control()

    def update(self):
        #self.sprite_in_control.update()
        self.all_players.update()

    def draw(self):
        self.screen.fill(MARINHO)
        self.all_players.draw(self.screen)
        pygame.display.flip()

    def change_sprite_control(self):
        # pass
        # if self.sprite_in_control:
        #     self.sprite_in_control.image.fill(GREEN)
        self.sprite_in_control = random.choice(self.all_players.sprites())  # random.choice(self.players_list)
        # self.sprite_in_control.image.fill(YELLOW)


g = Game()
while g.running:
    g.new()

pygame.quit()
