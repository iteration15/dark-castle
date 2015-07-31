import pygame, math, sys, random, pickle
from pygame.locals import *
from random import randint, choice

from constants import *

class Map(object):
    def __init__(self):
        self.cleared = self.get_blank_map()
        self.current = self.get_blank_map()
        self.walls = self.get_blank_map()
        self.hero = (0,0)
        self.fill_map()

    def fill_map(self):
        for i in range(ROWS)
            for j in range(COLUMNS):
                if not self.floor[i][j]:
                    self.walls[i][j] = 1

    def get_blank_map(self):
        map = []
        for i in range(ROWS):
            row = []
            for j in range(COLUMNS):
                row.append(0)
                map.append(row)
        return map
    
