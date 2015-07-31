from os.path import abspath, dirname, join, sep

MOVE_SIZE = 12
RADIUS = 2
START_Y = 140
START_X = 100
DIS_Y = 1024
DIS_X = 1024
COLUMNS = 16
ROWS = 21
TILE_SIZE = 48
RFONT_SIZE = 48
SFONT_SIZE = 20
DIRECTIONS = ['North','South','East','West']
LONG_STRING = "X" * 50

IMG_DIR = join(dirname(dirname(abspath(__file__))),"graphics") + sep

IMG_BG_LVL1 = 'bglvl1.png'
IMG_HERO_D = 'hero_down.png'
