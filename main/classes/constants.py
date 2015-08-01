from os.path import abspath, dirname, join, sep

MOVE_SIZE = 12
RADIUS = 2
START_Y = 140 #vert
START_X = 100 #hori
DIS_Y = 800
DIS_X = 800
COLUMNS = 100
ROWS = 100
TILE_SIZE = 20
MOVERATE = 5
RFONT_SIZE = 48
SFONT_SIZE = 20
DIRECTIONS = ['North','South','East','West']
LONG_STRING = "X" * 50
BLACK = (0,0,0)
HALF_WINWIDTH = int(DIS_Y // 2)
HALF_WINHEIGHT = int(DIS_X // 2)
MAXHEALTH = 3

IMG_DIR = join(dirname(dirname(abspath(__file__))),"graphics") + sep
#DISPLAYSURF = pygame.display.set_mode((DIS_X, DIS_Y))

IMG_WALL = 'wall.png'
IMG_FLOOR = 'floor.png'
IMG_BG_LVL1 = 'bglvl1.png'
IMG_HERO_D = 'hero_down.png'

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
