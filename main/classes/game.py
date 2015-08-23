import pygame, sys, pickle
from pygame.locals import *

from constants import *
from gamescreen import GameScreen
from wall import Wall

class Game(object):

    def __init__(self):
        #initialize GameScreen
        self.gamescreen = GameScreen()

        all_sprite_list = pygame.sprite.Group()
        wall_list = pygame.sprite.Group()
        myWall = Wall(0, 0, 10, 600)
        self.gamescreen.drawWall(myWall)
      
        self.runGame()

    def runGame(self):
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False
        gameOverMode = False

        cameraX = 0
        cameraY = 0

        heroImg = IMG_HERO_D

        heroObj = {'surf'     : heroImg,
                             'x'           : START_X,
                             'y'           : START_Y,
                             'health' : MAXHEALTH}
        
        # main game loop
        while True:
            # draw background here prevents sprite duplication
            self.gamescreen.drawBackground()

            heroX = heroObj['x']
            heroY = heroObj['y']

            if (cameraX + START_X) - heroX > CAMERASLACK:
                cameraX = heroX + CAMERASLACK - START_X
                #cameraX = heroX - START_X
            elif heroX - (cameraX + START_X) > CAMERASLACK:
                cameraX = heroX - CAMERASLACK - START_X
            if (cameraY + START_Y) - heroY > CAMERASLACK:
                cameraY = heroY + CAMERASLACK - START_Y
            elif heroY - (cameraY + START_Y) > CAMERASLACK:
                cameraY = heroY - CAMERASLACK - START_Y

            self.gamescreen.drawCamera(cameraX, cameraY)
           
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.endGame()                  
                elif event.type == KEYDOWN:
                    if event.key in (K_UP, K_w) :
                        #setting other directions to False
                        #gets rid of the diagonal issue
                       moveDown = False
                       moveUp = True
                       moveLeft = False
                       moveRight = False
                    elif event.key in (K_DOWN, K_s):
                        moveUp = False
                        moveDown = True
                        moveLeft = False
                        moveRight = False
                    elif event.key in (K_LEFT, K_a):
                        moveRight = False
                        moveLeft = True
                        moveUp = False
                        moveDown = False
                    elif event.key in (K_RIGHT, K_d):
                        moveLeft = False
                        moveRight = True
                        moveUp = False
                        moveDown = False
                        
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
                    self.gamescreen.heroWalk((heroObj['x'], heroObj['y']), IMG_HERO_L1)
                if moveRight:
                    heroObj['x'] += MOVERATE 
                    self.gamescreen.heroWalk((heroObj['x'], heroObj['y']), IMG_HERO_R1)
                if moveUp:
                    heroObj['y'] -= MOVERATE 
                    self.gamescreen.heroWalk((heroObj['x'], heroObj['y']), IMG_HERO_U1)
                if moveDown:
                    heroObj['y'] += MOVERATE 
                    self.gamescreen.heroWalk((heroObj['x'], heroObj['y']), IMG_HERO_D)
                        
    def endGame(self):
        pygame.quit()
        sys.exit(0)
