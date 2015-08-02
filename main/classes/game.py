import pygame, sys, pickle
from pygame.locals import *

from constants import *
from gamemap import Map
from gamescreen import GameScreen
from hero import Hero

class Game(object):

    def __init__(self):
        #initialize GameScreen
        self.gamescreen = GameScreen()
        #initialize Map
        self.map = Map()
        #initialize Hero
        #self.hero = Hero()

        self.clock = pygame.time.Clock()
        self.direction = 0

        self.gamescreen.draw_screen_layers(map=self.map)
        
        self.runGame()

    def refresh_screen(self):
        self.gamescreen.draw_hero(self.map.hero)
        self.gamescreen.draw_screen_layers(self.map)

    def runGame(self):
        heroX = 0
        heroY = 0
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        gameOverMode = False

        heroImg = IMG_HERO_D

        DISPLAYSURF = pygame.display.set_mode((DIS_X, DIS_Y))

        heroObj = {'surf' : heroImg,
                             'x' : START_X,
                             'y' : START_Y,
                             'health' : MAXHEALTH}
        
        # main game loop
        while True:
            self.clock.tick(30)
            heroMoveTo = None

            # draw background
            self.gamescreen.draw_background()

            # draw hero
            if not gameOverMode:
                self.gamescreen.draw_hero((heroObj['x'], heroObj['y']), heroObj['surf'])
            
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
                    #heroObj['surf'] = 
                if moveRight:
                   heroObj['x'] += MOVERATE
                if moveUp:
                    heroObj['y'] -= MOVERATE
                if moveDown:
                    heroObj['y'] += MOVERATE
                
            pygame.display.update()
                        
    def endGame(self):
        pygame.quit()
        sys.exit(0)
