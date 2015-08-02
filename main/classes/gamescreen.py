import pygame

from constants import *

class GameScreen(object):
    def __init__(self):
        self.selected_tile = [0,0]
        self.screen = pygame.display.set_mode((DIS_Y, DIS_X))
        self.font = pygame.font.SysFont(None,RFONT_SIZE)
        self.small_font = pygame.font.SysFont(None,SFONT_SIZE)
        
        #load lvl 1 background
        self.bg = pygame.image.load(IMG_DIR + IMG_BG_LVL1)
        
        self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_D)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_D3)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_L1)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_L2)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_L3)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_R1)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_R2)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_R3)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_U1)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_U2)
        #self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_U3)
        
        self.draw_background()

        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(self.bg,(0,0))

    def draw_hero(self, coord, heroImg):
        self.screen.blit(self.hero_blit, coord)

    def draw_screen_layers(self, map):
        self.draw_background()

        pygame.display.flip()




                        
    
    
