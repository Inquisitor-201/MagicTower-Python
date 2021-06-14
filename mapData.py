import constants as c

mp_data = {0:
[
    [1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 2, 0, 0, 2, c.STAIRS_UP, 2, 0, 0, 2, 2, 1],
    [1, 2, 0, 0, 0, 2, c.M_SLIME, 2, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 2, 2, 2, 2, 2, c.STEEL_GATE, 2, 2, 2, 2, 2, 1],
    [1, 2, 4, 2, 4, 2, 0, 2, 4, 2, 4, 2, 1],
    [1, 4, 4, 4, 4, 2, 0, 2, 4, 4, 4, 4, 1],
    [1, 4, 4, 4, 4, 2, 0, 2, 4, 4, 4, 4, 1],
    [1, 4, 4, 4, 4, 2, 0, 2, 4, 4, 4, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],

1: [
    [1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 0, c.M_SLIME, 0, 0, c.STAIRS_DOWN, 2, c.STAIRS_UP, 0, 2, 2, 1],
    [1, 2, 2, c.M_RED_SLIME, 2, 2, 2, 2, 2, c.M_BAT, 2, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 2, c.M_SLIME, c.M_RED_SLIME, c.M_SLIME, 2, 1],
    [1, 2, c.M_BAT, 2, 2, 2, 0, c.M_BAT, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 2, 2, c.M_RED_SLIME, 2, 2, 1],
    [1, 2, 2, c.BLUE_GATE, 2, 2, 0, c.YELLOW_GATE, 0, 0, 0, 2, 1],
    [1, 2, c.M_SLIME, 0, c.M_SLIME, 2, c.M_SLIME, 2, 2, 2, c.YELLOW_GATE, 2, 1],
    [1, 2, c.RED_BOTTLE, c.M_ORC, c.RED_BOTTLE, 2, 0, 2, 0, 0, c.M_SKELETON, 2, 1],
    [1, 2, c.RED_GEM, c.YELLOW_KEY, c.BLUE_GEM, 2, 0, 2, c.RED_KEY, c.YELLOW_KEY, c.YELLOW_KEY, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],

2: [
    [1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, c.RED_GEM, c.BLUE_GEM, 0, 2, 0, 2, c.STAIRS_DOWN, 2, 2, 2, 1],
    [1, 2, c.RED_BOTTLE, c.BLUE_BOTTLE, 0, 2, 0, 2, 0, 0, 2, 2, 1],
    [1, 2, 0, c.M_SKELETON_CAPTAIN, 0, c.M_RED_BAT, c.STEEL_GATE, 2, 2, c.M_RED_SLIME, 2, 2, 1],
    [1, 2, 2, c.RED_GATE, 2, 2, 2, 2, 0, 0, 0, 2, 1],
    [1, 2, 0, c.M_KNIGHT, 0, c.RED_GATE, 0, c.BLUE_KEY, 0, 2, 0, 2, 1],
    [1, 2, c.YELLOW_GATE, 2, c.YELLOW_GATE, 2, 2, 2, c.M_SLIME, 2, c.M_BAT, 2, 1],
    [1, 2, 0, 2, c.RED_GEM, 0, 0, 2, c.M_SLIME, 2, c.M_BAT, 2, 1],
    [1, 2, c.RED_KEY, 2, c.BLUE_GEM, 0, c.YELLOW_KEY, 2, 0, 2, c.BLUE_BOTTLE, 2, 1],
    [1, 2, c.RED_KEY, 2, 0, c.BLUE_KEY, 0, 2, c.STAIRS_UP, 2, c.STAIRS_UP, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],

3: [
    [1, 1, 1, 1, 1, 9, 9, 9, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, c.STAIRS_UP, 0, c.M_BAT, 2, 0, 0, c.M_MAGE, c.BLUE_GATE, c.BLUE_GEM, 2, 1],
    [1, 2, 0, 2, 0, 2, c.M_RED_SLIME, 2, 2, 2, 0, 2, 1],
    [1, 2, c.M_BAT, 0, 0, c.M_RED_SLIME, c.M_BAT, 0, 0, 2, 0, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 1],
    [1, c.STAIRS_UP, 0, 0, c.M_BAT, 0, 0, c.BLUE_GATE, 0, 2, 0, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 0, 2, c.YELLOW_GATE, 2, 1],
    [1, 2, 2, c.SHOP_LEFT, c.SHOP, c.SHOP_RIGHT, 0, 2, 0, 2, c.M_SKELETON, 2, 1],
    [1, 2, c.STAIRS_UP, c.M_SLIME, c.M_RED_SLIME, 0, 0, c.M_RED_SLIME, 0, 2, 0, 2, 1],
    [1, 2, 2, c.BLUE_BOTTLE, 0, 0, 0, 2, c.STAIRS_DOWN, 2, c.STAIRS_DOWN, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],


}

"""
GROUND = 0
E_WALL = 1
WALL_WHITE = 2
WALL_BROWN = 3
LAVA = 4
STAIRS_UP = 7
STAIRS_DOWN = 8
BLACK_BLOCK = 9

YELLOW_KEY = 10
BLUE_KEY = 11
RED_KEY = 12
COIN = 13
RED_BOTTLE = 14
BLUE_BOTTLE = 15
RED_GEM = 16
BLUE_GEM = 17

YELLOW_GATE = 30
BLUE_GATE = 31
RED_GATE = 32
STEEL_GATE = 33
"""
