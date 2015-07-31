from os.path import abspath, dirname, join, sep

MOVEMENT_SIZE = 12
RADIUS = 2
COLUMNS = 16
ROWS = 21
TILE_SIZE = 48
DIRECTIONS = ['North','South','East','West']
LONG_STRING = "X" * 50

IMG_DIR = join(dirname(dirname(abspath(__file__))),"graphics") + sep
