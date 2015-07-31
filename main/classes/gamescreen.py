import pygame

from constants import *

class GameScreen(object):
    def __init__(self):
        self.selected_tile = [0,0]
        self.screen = pygame.display.set_mode((1024,1024))
        self.font = pygame.font.SysFont(None,48)
        self.font = pygame.font.SysFont(None,20)
        self.bg = pygame.image.load(IMG_DIR + 'bglvl1.png')
        self.draw_background()
        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(self.bg,(0,0))

    def draw_screen_layers(self, map, player_stats):
        self.draw_background()
        pygame.display.flip()
    
    
