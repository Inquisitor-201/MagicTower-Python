import pygame as pg
import scene
import gameAttributes as g

if __name__ == '__main__':
    pg.display.set_caption('新新魔塔')
    pg.display.set_icon(pg.image.load('./Resources/Icons/Item01-08_2_1.png'))
    pg.init()
    game = scene.GameScene()
