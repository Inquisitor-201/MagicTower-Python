import pygame as pg
import os.path
import constants as c
import gameAttributes as b
import items


class ViewManager:
    def __init__(self):
        self.src_imgs = {}
        self.img = {}
        self.current_index = {}  # 当前动图序号
        self.frame_count = 0

        self.sourcePath = './Resources/Characters'
        self.src_imgs['ground'] = self.load(self.sourcePath, 'Other09.png')
        self.src_imgs['e_wall'] = self.load(self.sourcePath, 'Wall.png')
        self.src_imgs['walls'] = self.load(self.sourcePath, 'Event01-Wall01.png')
        self.src_imgs['common'] = self.load(self.sourcePath, 'common.png')
        self.src_imgs['braver'] = self.load(self.sourcePath, 'Actor01-Braver09.png')
        self.src_imgs['keys'] = self.load(self.sourcePath, 'Item01-01.png')
        self.src_imgs['coins'] = self.load(self.sourcePath, 'Item01-11.png')
        self.src_imgs['bottles'] = self.load(self.sourcePath, 'Item01-02.png')
        self.src_imgs['gems'] = self.load(self.sourcePath, 'Item01-Gem01.png')
        self.src_imgs['gates'] = self.load(self.sourcePath, 'Event01-Door01.png')
        self.src_imgs['m_slimes'] = self.load(self.sourcePath, 'Monster01-01.png')
        self.src_imgs['m_skeletons'] = self.load(self.sourcePath, 'Monster02-01.png')
        self.src_imgs['m_bats'] = self.load(self.sourcePath, 'Monster03-01.png')
        self.src_imgs['m_orcs'] = self.load(self.sourcePath, 'Monster09-01.png')
        self.src_imgs['m_mages'] = self.load(self.sourcePath, 'Monster06-01.png')
        self.src_imgs['m_knights'] = self.load(self.sourcePath, 'Monster07-01.png')

        self.src_imgs['shop_dialogue'] = self.load(self.sourcePath, 'Shop.png')

        self.img[c.GROUND] = ('ground', 1, [(0, 0)])
        self.img[c.E_WALL] = ('e_wall', 1, [(0, 0)])
        self.img[c.WALL_WHITE] = ('walls', 1, [(0, 2)])
        self.img[c.WALL_BROWN] = ('walls', 1, [(0, 1)])
        self.img[c.LAVA] = ('common', 2, [(16, 4), (16, 5)])
        self.img[c.STAIRS_UP] = ('common', 1, [(16, 3)])
        self.img[c.STAIRS_DOWN] = ('common', 1, [(16, 2)])
        self.img[c.BLACK_BLOCK] = ('e_wall', 1, [(0, 1)])

        self.img[c.YELLOW_KEY] = ('keys', 1, [(0, 0)])
        self.img[c.BLUE_KEY] = ('keys', 1, [(0, 1)])
        self.img[c.RED_KEY] = ('keys', 1, [(0, 2)])
        self.img[c.COIN] = ('coins', 1, [(0, 0)])
        self.img[c.RED_BOTTLE] = ('bottles', 1, [(0, 0)])
        self.img[c.BLUE_BOTTLE] = ('bottles', 1, [(0, 1)])
        self.img[c.RED_GEM] = ('gems', 1, [(0, 0)])
        self.img[c.BLUE_GEM] = ('gems', 1, [(0, 1)])
        self.img[c.YELLOW_GATE] = ('gates', 1, [(0, 0)])
        self.img[c.BLUE_GATE] = ('gates', 1, [(0, 1)])
        self.img[c.RED_GATE] = ('gates', 1, [(0, 2)])
        self.img[c.STEEL_GATE] = ('walls', 1, [(0, 3)])
        self.img[c.SHOP_LEFT] = ('common', 1, [(11, 6)])
        self.img[c.SHOP_RIGHT] = ('common', 1, [(11, 8)])
        self.img[c.SHOP] = ('common', 2, [(11, 7), (11, 9)])

        self.img[c.BRAVER] = ('braver', 16, [(0, 0), (0, 1), (0, 2), (0, 3),
                                             (1, 0), (1, 1), (1, 2), (1, 3),
                                             (2, 0), (2, 1), (2, 2), (2, 3),
                                             (3, 0), (3, 1), (3, 2), (3, 3)])

        self.img[c.M_SLIME] = ('m_slimes', 4, [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.img[c.M_RED_SLIME] = ('m_slimes', 4, [(1, 0), (1, 1), (1, 2), (1, 3)])
        self.img[c.M_BLACK_SLIME] = ('m_slimes', 4, [(2, 0), (2, 1), (2, 2), (2, 3)])
        self.img[c.M_SLIME_KING] = ('m_slimes', 4, [(3, 0), (3, 1), (3, 2), (3, 3)])
        self.img[c.M_SKELETON] = ('m_skeletons', 4, [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.img[c.M_MAGE] = ('m_mages', 4, [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.img[c.M_BAT] = ('m_bats', 4, [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.img[c.M_BIG_BAT] = ('m_bats', 4, [(1, 0), (1, 1), (1, 2), (1, 3)])
        self.img[c.M_RED_BAT] = ('m_bats', 4, [(2, 0), (2, 1), (2, 2), (2, 3)])
        self.img[c.M_ORC] = ('m_orcs', 4, [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.img[c.M_SKELETON_CAPTAIN] = ('m_skeletons', 4, [(2, 0), (2, 1), (2, 2), (2, 3)])
        self.img[c.M_KNIGHT] = ('m_knights', 4, [(0, 0), (0, 1), (0, 2), (0, 3)])

        for i in range(c.TOTAL_ITEMS):
            self.current_index[i] = 0

        self.damage_data = [[0 for i in range(13)] for j in range(13)]
        print(self.damage_data)

    @staticmethod
    def load(path, filename):
        return pg.image.load(os.path.join(path, filename))

    def draw(self, screen, item_id, pos, index=None):
        src, frames, region = self.img[item_id]
        c_index = self.current_index[item_id]
        reg = region[c_index] if index is None else region[index]
        screen.blit(self.src_imgs[src], (pos[0], pos[1]), (32*reg[1], 32*reg[0], 32, 32))

    def draw_by_rel_pos(self, screen, item_id, pos, index=None):
        src, frames, region = self.img[item_id]
        c_index = self.current_index[item_id]
        reg = region[c_index] if index is None else region[index]
        screen.blit(self.src_imgs[src], (192+pos[0]*32, pos[1]*32), (32*reg[1], 32*reg[0], 32, 32))

    def update_index(self):  # 更新动图的序号
        self.frame_count += 1
        if self.frame_count % 6 == 0:
            for item_id in range(c.TOTAL_ITEMS):
                if item_id in self.img.keys():
                    frames = self.img[item_id][1]
                    self.current_index[item_id] = (self.current_index[item_id] + 1) % frames
        if self.frame_count == 96:
            self.frame_count = 0

    @staticmethod
    def print_text(screen, font_family, text, pos, zihao=22, color=c.COLOR_WHITE):
        fontObj = pg.font.SysFont(font_family, zihao)
        textSurfaceObj = fontObj.render(text, False, color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = pos
        screen.blit(textSurfaceObj, textRectObj)

    def print_attributes(self, screen):
        self.draw(screen, c.BRAVER, (45, 37), index=0)
        self.print_text(screen, 'Kaiti', '第 ' + str(b.CURRENT_FLOOR) + ' 层', (400, 15))

        self.draw(screen, c.BRAVER, (45, 37), index=0)
        self.print_text(screen, 'Kaiti', '*'+c.status2str[b.STATUS]+'*', (120, 55))

        self.print_text(screen, 'Kaiti', '等级：', (70, 93))
        self.print_text(screen, 'Comic Sans MS', str(b.LEVEL), (142, 93))
        self.print_text(screen, 'Kaiti', '体力：', (70, 122))
        self.print_text(screen, 'Comic Sans MS', str(b.HP), (142, 122))
        self.print_text(screen, 'Kaiti', '攻击：', (70, 151))
        self.print_text(screen, 'Comic Sans MS', str(b.ATK), (142, 151))
        self.print_text(screen, 'Kaiti', '防御：', (70, 180))
        self.print_text(screen, 'Comic Sans MS', str(b.DEF), (142, 180))
        self.print_text(screen, 'Kaiti', '敏捷：', (70, 209))
        self.print_text(screen, 'Comic Sans MS', str(b.AGI), (142, 209))
        self.print_text(screen, 'Kaiti', '经验值：', (70, 238))
        self.print_text(screen, 'Comic Sans MS', str(b.EXP), (142, 238))

        self.draw(screen, c.YELLOW_KEY, (45, 265), index=0)
        self.print_text(screen, 'Kaiti', '×', (95, 283))
        self.print_text(screen, 'Comic Sans MS', str(b.YELLOW_KEY), (142, 280))

        self.draw(screen, c.BLUE_KEY, (45, 295), index=0)
        self.print_text(screen, 'Kaiti', '×', (95, 313))
        self.print_text(screen, 'Comic Sans MS', str(b.BLUE_KEY), (142, 310))

        self.draw(screen, c.RED_KEY, (45, 325), index=0)
        self.print_text(screen, 'Kaiti', '×', (95, 343))
        self.print_text(screen, 'Comic Sans MS', str(b.RED_KEY), (142, 340))

        self.draw(screen, c.COIN, (44, 355), index=0)
        self.print_text(screen, 'Kaiti', '×', (95, 373))
        self.print_text(screen, 'Comic Sans MS', str(b.GOLD), (142, 370))

    def show_damages(self, screen):
        if self.frame_count % 12 == 0:
            for row in range(13):
                for col in range(13):
                    if b.floorData[row][col] in items.item_info.keys():
                        cur_item = items.item_info[b.floorData[row][col]]
                        if cur_item.item_type == c.I_MONSTER:
                            _, self.damage_data[row][col] = cur_item.calc_damage()
                            self.print_text(screen, 'Comic Sans MS', str(self.damage_data[row][col]),
                                            pos=(208+col*32, row*32-3),
                                            zihao=12,
                                            color=c.COLOR_RED if self.damage_data[row][col]>=b.HP else c.COLOR_WHITE)
        else:
            for row in range(13):
                for col in range(13):
                    if b.floorData[row][col] in items.item_info.keys():
                        cur_item = items.item_info[b.floorData[row][col]]
                        if cur_item.item_type == c.I_MONSTER:
                            self.print_text(screen, 'Comic Sans MS', str(self.damage_data[row][col]),
                                            pos=(208+col*32, row*32-3),
                                            zihao=12,
                                            color=c.COLOR_RED if self.damage_data[row][col]>=b.HP else c.COLOR_WHITE)

                    # (192+pos[0]*32, pos[1]*32)