import pygame, sys, pickle
from pygame.locals import *

from constants import *
from gamescreen import GameScreen

class Game(object):

    def __init__(self):
        #initialize GameScreen
        self.gamescreen = GameScreen()
       
        self.runGame()

    def runGame(self):
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        gameOverMode = False

        heroImg = IMG_HERO_D

        heroObj = {'surf' : heroImg,
                             'x' : START_X,
                             'y' : START_Y,
                             'health' : MAXHEALTH}
        
        # main game loop
        while True:
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
                    heroObj['surf'] = IMG_HERO_L1
                if moveRight:
                   heroObj['x'] += MOVERATE
                   heroObj['surf'] = IMG_HERO_R1
                if moveUp:
                    heroObj['y'] -= MOVERATE
                    heroObj['surf'] = IMG_HERO_U1
                if moveDown:
                    heroObj['y'] += MOVERATE
                    heroObj['surf'] = IMG_HERO_D                
            pygame.display.update()
                        
    def endGame(self):
        pygame.quit()
        sys.exit(0)
