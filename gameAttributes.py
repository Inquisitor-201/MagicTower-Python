import constants as c
from mapData import *

HP = 1000
ATK = 10
DEF = 10
AGI = 2

LEVEL = 1
EXP = 0

POS_R = 11
POS_C = 6

GOLD = 0
YELLOW_KEY = 1
BLUE_KEY = 1
RED_KEY = 1

DIRECTION = c.D_UP
STATUS = c.S_NORMAL

CURRENT_FLOOR = 0

SHOP_PRICE = 20
SHOP_PRICE_INCREMENT = 1

floorData = []
SHOW_DAMAGE = True


def change_floor(new_floor):
    global CURRENT_FLOOR, floorData
    CURRENT_FLOOR = new_floor
    floorData = mp_data[new_floor]
