import pygame

from constants import *

def loadImage(name):
    image = pygame.image.load(IMG_DIR + name)
    return image

class GameScreen(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((DIS_Y, DIS_X))
        self.font = pygame.font.SysFont(None,RFONT_SIZE)
        self.small_font = pygame.font.SysFont(None,SFONT_SIZE)
        
        #load lvl 1 background
        self.bg = pygame.image.load(IMG_DIR + IMG_BG_LVL1)
        self.hero = pygame.image.load(IMG_DIR + IMG_HERO_D)
        
        self.index = 0

        self.moveDown = []
        self.moveDown.append(loadImage(IMG_HERO_D))
        self.moveDown.append(loadImage(IMG_HERO_D3))

        self.moveLeft = []
        self.moveLeft.append(loadImage(IMG_HERO_L1))
        self.moveLeft.append(loadImage(IMG_HERO_L2))
        self.moveLeft.append(loadImage(IMG_HERO_L3))

        self.moveRight = []
        self.moveRight.append(loadImage(IMG_HERO_R1))
        self.moveRight.append(loadImage(IMG_HERO_R2))
        self.moveRight.append(loadImage(IMG_HERO_R3))

        self.moveUp = []
        self.moveUp.append(loadImage(IMG_HERO_U1))
        self.moveUp.append(loadImage(IMG_HERO_U2))
        self.moveUp.append(loadImage(IMG_HERO_U3))

        # draw for initial state
        self.drawBackground()
        self.drawHero()

        pygame.display.flip()

    def drawBackground(self):
        self.screen.blit(self.bg,(0,0))

    def drawCamera(self, cameraX, cameraY, heroX, heroY):
        self.screen.blit(self.bg,(0 - cameraX, 0 - cameraY))
        
    def drawHero(self):
        self.screen.blit(self.hero,(START_X, START_Y))
        #pygame.display.flip()
        #pygame.display.update()

    def heroWalk(self, coord, heroImg):
        if heroImg == IMG_HERO_D:
            self.index += 1
            if self.index >= len(self.moveDown):
                self.index = 0
            self.image = self.moveDown[self.index]
            self.screen.blit(self.image, coord)
            pygame.display.update()
        elif heroImg == IMG_HERO_L1:
            self.index += 1
            if self.index >= len(self.moveLeft):
                self.index = 0
            self.image = self.moveLeft[self.index]
            self.screen.blit(self.image, coord)
            pygame.display.update()
        elif heroImg == IMG_HERO_R1:
            self.index += 1
            if self.index >= len(self.moveRight):
                self.index = 0
            self.image = self.moveRight[self.index]
            self.screen.blit(self.image, coord)
            pygame.display.update()
        elif heroImg == IMG_HERO_U1:
            self.index += 1
            if self.index >= len(self.moveUp):
                self.index = 0
            self.image = self.moveUp[self.index]
            self.screen.blit(self.image, coord)
        pygame.display.update()
        pygame.display.flip()
        
    def draw_screen_layers(self):
        self.draw_background()

