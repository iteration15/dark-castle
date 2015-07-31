import pygame, sys, pickle
from pygame.locals import *

from constants import *
from gamemap import Map
from gamescreen import GameScreen
from hero import Hero

class Game(object):

    def __init__(self):
        self.gamescreen = GameScreen()
        self.bg = pygame.image.load(IMG_DIR + 'bglvl1.png')

        self.map = Map()
        self.map.hero = (140,100)
        self.hero_stats = Hero()

        self.clock = pygame.time.Clock()
        self.direction = 0

        self.map.set_current_position(self.map.hero)
        
        self.run()

    def move(self, hor, vert):
        self.old_row, self.old_col = self.map.hero
        row = self.old_row + hor
        col = self.old_col + vert
        if row > (ROWS-1) * TILE_SIZE or row < 0 or col > (COLUMNS-1) * TILE_SIZE or col < 0:
            return
        if self.map.has_wall(row, col):
            return
        self.map.hero = (row, col)
        self.map.clear_block(self.map.player)
        self.map.set_current_position(self.map.hero)

    def refresh_screen(self):
        self.gamescreen.draw_hero(self.map.hero)
        self.gamescreen.draw_screen_layers(self.map, self.hero_stats)

    def run(self):
        hor = 0
        vert = 0
        while 1:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    if event.key == K_LEFT:
                        hor = -TILE_SIZE
                        vert = 0
                    if event.key == K_RIGHT:
                        hor = TILE_SIZE
                        vert = 0
                    if event.key == K_UP:
                        vert = -TILE_SIZE
                        hor = 0
                    if event.key == K_DOWN:
                        vert = TILE_SIZE
                        hor = 0
                if event.type == KEYUP:
                    if vert or hor:
                        self.move(hor, vert)
                        hor = 0
                        vert = 0
            self.refresh_screen()
                        
    def end_game(self):
        sys.exit()













    
