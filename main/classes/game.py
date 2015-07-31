import pygame, sys, pickle
from pygame.locals import *

from constants import *
from gamemap import Map
from gamescreen import GameScreen
from hero import Hero

class Game(object):

    def __init__(self):
        self.screen = GameScreen()
        self.bg = pygame.image.load(IMG_DIR + 'bglvl1.png')

        self.map = Map()
        self.map.hero = (1*TILE_SIZE, 1*TILE_SIZE)


    def end_game(self):
        sys.exit()

    
