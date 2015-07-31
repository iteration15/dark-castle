import pygame

from constants import *

class GameScreen(object):
    def __init__(self):
        self.selected_tile = [0,0]
        self.screen = pygame.display.set_mode((1024,1024))
        self.font = pygame.font.SysFont(None,48)
        self.font = pygame.font.SysFont(None,20)
        self.bg = pygame.image.load(IMG_DIR + 'bglvl1.png')
        self.hero_blit = pygame.image.load(IMG_DIR + 'hero_down.png')
        self.draw_background()
        self.draw_hero((140,100))
        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(self.bg,(0,0))

    def draw_hero(self, coord):
        self.screen.blit(self.hero_blit, coord)

    def draw_screen_layers(self, map, hero_stats):
        self.draw_background()
        self.draw_hero(coord=map.hero)
        pygame.display.flip()
    
    
