import pygame, math, sys, random, pickle
from pygame.locals import *
from random import randint, choice

from constants import *

class Map(object):
    def __init__(self):
        self.cleared = self.get_blank_map()
        self.current = self.get_blank_map()
        self.walls = self.get_blank_map()
        self.hero = (START_Y, START_X)
        self.floor = self.get_blank_map()
        self.fill_map()

    def fill_map(self):
        for i in range(ROWS):
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

    def has_wall(self, row, col):
        row = row // TILE_SIZE
        col = col // TILE_SIZE
        if self.walls[row][col]:
            return True
        else:
            return False

    def clear_block(self, position):
        x, y = position
        col = y // TILE_SIZE
        row = x // TILE_SIZE

        self.cleared[row][col] = 1
        if row < ROWS-1:
            self.cleared[row+1][col] = 1
        if row > 0:
            self.cleared[row-1][col] = 1
        if col < COLUMNS-1:
            self.cleared[row][col+1] = 1
        if col > 0:
            self.cleared[row][col-1] = 1

    def set_current_position(self, position):
        self.current = self.get_blank_map()
        row, col = position
        row = row // TILE_SIZE 
        col = col // TILE_SIZE
        self.current[row][col] = 0
        for i in range(RADIUS):
            if row-i > 0:
                self.current[row-i-1][col] = 1
            if row+i < ROWS-1:
                self.current[row+i+1][col] = 1
            if col-i > 0:
                self.current[row][col-i-1] = 1
            if col+i < COLUMNS-1:
                self.current[row][col+i+1] = 1
        for i in range(RADIUS-1):
            if row-i > 0 and col-i > 0: self.current[row-i-1][col-i-1] = 1
            if row-i > 0 and col-i < COLUMNS-1: self.current[row-i-1][col+i+1] = 1
            if row+i < ROWS-1 and col-i > 0: self.current[row+i+1][col-i-1] = 1
            if row+i < ROWS-1 and col+i < COLUMNS-1: self.current[row+i+1][col+i+1] = 1
            


            
    
