import pygame

from constants import *

class GameScreen(object):
    def __init__(self):
        self.selected_tile = [0,0]
        self.screen = pygame.display.set_mode((DIS_Y, DIS_X))
        self.font = pygame.font.SysFont(None,RFONT_SIZE)
        self.small_font = pygame.font.SysFont(None,SFONT_SIZE)
        self.bg = pygame.image.load(IMG_DIR + IMG_BG_LVL1)
        self.hero_blit = pygame.image.load(IMG_DIR + IMG_HERO_D)
        self.wall_tile = pygame.image.load(IMG_DIR + IMG_WALL)
        self.floor_tile = pygame.image.load(IMG_DIR + IMG_FLOOR)
        self.draw_background()
        self.draw_hero((START_Y, START_X))
        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(self.bg,(0,0))

    def draw_hero(self, coord):
        self.screen.blit(self.hero_blit, coord)

    def draw_screen_layers(self, map, hero_stats):
        self.draw_walls(map.floor, self.floor_tile)
        self.draw_walls(map.walls, self.wall_tile)
        self.draw_background()
        self.draw_hero(coord=map.hero)
        pygame.display.flip()

    def draw_walls(self, walls, tile):
        for row in range(ROWS):
            for col in range(COLUMNS):
                    if walls[row][col] != 0:
                        self.screen.blit(tile, (row*TILE_SIZE, col*TILE_SIZE))

    def draw_darkness(self, map):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if map.cleared[row][col] == 0:
                    if not map.current[row][col]:
                        pygame.draw.rect(self.screen, BLACK, (row*TILE_SIZE, col*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                if map.cleared[row][col] == 1:
                    if not map.current[row][col]:
                        shadow = pygame.Surface((TILE_SIZE, TILE_SIZE))
                        shadow.set_alpha(200)
                        shadow.fill(BLACK)
                        self.screen.blit(shadow, (row*TILE_SIZE, col*TILE_SIZE))

                        
    
    
