import pygame, sys, pickle
from pygame.locals import *

from constants import *
from gamemap import Map
from gamescreen import GameScreen
from hero import Hero

class Game(object):

    def __init__(self):
        #initializes GameScreen
        self.gamescreen = GameScreen()
        #initializes Map
        self.map = Map()
        #initializes Hero
        self.hero_stats = Hero()

        self.clock = pygame.time.Clock()
        self.direction = 0

        #self.map.clear_block(self.map.hero)
        
        #self.map.set_current_position(self.map.hero)

        self.gamescreen.draw_screen_layers(map=self.map, hero_stats=self.hero_stats)
        
        self.runGame()

    def moveHero(self, heroX, heroY):
        self.old_row, self.old_col = self.map.hero
        row = self.old_row + heroX
        col = self.old_col + heroY
        if row > (ROWS-1) * TILE_SIZE or row < 0 or col > (COLUMNS-1) * TILE_SIZE or col < 0:
            return
        if self.map.has_wall(row, col):
            return
        self.map.hero = (row, col)
        #self.map.clear_block(self.map.player)
        self.map.set_current_position(self.map.hero)

    def refresh_screen(self):
        self.gamescreen.draw_hero(self.map.hero)
        self.gamescreen.draw_screen_layers(self.map, self.hero_stats)

    def runGame(self):
        heroX = 0
        heroY = 0
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        gameOverMode = False

        DISPLAYSURF = pygame.display.set_mode((DIS_X, DIS_Y))

        heroObj = {'surface': pygame.image.load(IMG_DIR + IMG_HERO_D),
                             'facing': LEFT,
                             'x' : START_X,
                             'y' : START_Y,
                             'health' : MAXHEALTH}

        if not gameOverMode:
            self.gamescreen.draw_hero((heroObj['x'],heroObj['y']))

        # main game loop
        while True:
            self.clock.tick(30)
            heroMoveTo = None

            # draw background
            self.gamescreen.draw_background()

            # draw hero
            if not gameOverMode:
                self.gamescreen.draw_hero((heroObj['x'],heroObj['y']))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.endGame()
                    
                elif event.type == KEYDOWN:
                    if event.key in (K_UP, K_w) :
                       moveDown = False
                       moveUp = True
                    elif event.key in (K_DOWN, K_s):
                        moveUp = False
                        moveDown = True
                    elif event.key in (K_LEFT, K_a):
                        moveRight = False
                        moveLeft = True
                    elif event.key in (K_RIGHT, K_d):
                        moveLeft = False
                        moveRight = True
                        
                elif event.type == KEYUP:
                    if event.key in (K_LEFT, K_a):
                        moveLeft = False
                    elif event.key in (K_RIGHT, K_d):
                        moveRight = False
                    elif event.key in (K_UP, K_w):
                        moveUp = False
                    elif event.key in (K_DOWN, K_s):
                        moveDown = False
                    elif event.key == K_ESCAPE:
                        self.endGame()

            if not gameOverMode:
                if moveLeft:
                    heroObj['x'] -= MOVERATE
                if moveRight:
                   heroObj['x'] += MOVERATE
                if moveUp:
                    heroObj['y'] -= MOVERATE
                if moveDown:
                    heroObj['y'] += MOVERATE
                
            #self.refresh_screen()
            pygame.display.update()
                        
    def endGame(self):
        pygame.quit()
        sys.exit(0)

    











    
