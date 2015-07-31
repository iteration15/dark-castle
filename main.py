import pygame, math, sys, random
from pygame.locals import *

sys.path.append("main/classes")

from constants import *
from game import Game

def main():
    while 1:
        pygame.init()
        pygame.display.set_caption('Dark Castle')
        game = Game()

if __name__ == "__main__":
        main()
