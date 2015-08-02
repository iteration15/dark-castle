from os.path import abspath, dirname, join, sep

MOVE_SIZE = 12
RADIUS = 2
START_Y = 140 
START_X = 140
DIS_Y = 800
DIS_X = 800
COLUMNS = 100
ROWS = 100
TILE_SIZE = 20
MOVERATE = 3
RFONT_SIZE = 48
SFONT_SIZE = 20
DIRECTIONS = ['North','South','East','West']
LONG_STRING = "X" * 50
BLACK = (0,0,0)
MAXHEALTH = 3

IMG_DIR = join(dirname(dirname(abspath(__file__))),"graphics") + sep

IMG_BG_LVL1 = 'bglvl1.png'
IMG_HERO_D = 'hero_down.png'
IMG_HERO_D3 = 'hero_down3.png'
IMG_HERO_L1 = 'hero_left1.png'
IMG_HERO_L2 = 'hero_left2.png'
IMG_HERO_L3 = 'hero_left3.png'
IMG_HERO_R1 = 'hero_right1.png'
IMG_HERO_R2 = 'hero_right2.png'
IMG_HERO_R3 = 'hero_right3.png'
IMG_HERO_U1 = 'hero_up1.png'
IMG_HERO_U2 = 'hero_up2.png'
IMG_HERO_U3 = 'hero_up3.png'

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
openop
