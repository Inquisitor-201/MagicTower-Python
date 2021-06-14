import pygame as pg
import constants as c
from view import *


class ShopDialogue:
    def __init__(self):
        self.valid = False
        self.chosen_index = 0

    def print(self, screen):
        if self.valid:
            global vm
            screen.blit(vm.src_imgs['shop_dialogue'], (285, 76))
            vm.print_text(screen, 'Comic Sans MS', str(b.SHOP_PRICE), (379, 161), zihao=18, color=c.COLOR_YELLOW)
            vm.print_text(screen, 'Kaiti', '→', (330, 240+self.chosen_index*25), zihao=18, color=c.COLOR_YELLOW)

    def show(self):
        global dialogue_shown
        self.valid = True
        dialogue_shown = True
        self.chosen_index = 0

    def hide(self):
        global dialogue_shown
        self.valid = False
        dialogue_shown = False

    def move_up(self):
        if self.chosen_index > 0:
            self.chosen_index -= 1

    def move_down(self):
        if self.chosen_index < 3:
            self.chosen_index += 1

    def confirm(self):
        if self.chosen_index == 0:  # 500HP
            if b.GOLD >= b.SHOP_PRICE:
                b.GOLD -= b.SHOP_PRICE
                b.SHOP_PRICE += b.SHOP_PRICE_INCREMENT
                b.HP += 500
        elif self.chosen_index == 1:  # 3A
            if b.GOLD >= b.SHOP_PRICE:
                b.GOLD -= b.SHOP_PRICE
                b.SHOP_PRICE += b.SHOP_PRICE_INCREMENT
                b.ATK += 3
        elif self.chosen_index == 2:  # 3A
            if b.GOLD >= b.SHOP_PRICE:
                b.GOLD -= b.SHOP_PRICE
                b.SHOP_PRICE += b.SHOP_PRICE_INCREMENT
                b.DEF += 3
        elif self.chosen_index == 3:  # 3A
            self.hide()


def key_mode():
    global dialogue_shown
    if dialogue_shown:
        return c.KEY_MODE_SHOP
    else:
        return c.KEY_MODE_MAP


screen_size = (608, 416)
current_time = 0

screen = pg.display.set_mode(screen_size)
clock = pg.time.Clock()
vm = ViewManager()

dialogue_shown = False
dialogue_shop = ShopDialogue()
