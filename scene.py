import pygame as pg
import general as g
import constants as c
import gameAttributes as b
import items


class GameScene:
    def __init__(self):
        self.screen_size = (608, 416)
        self.Done = False
        self.keys = []

        b.change_floor(0)
        self.start_loop()

    def start_loop(self):
        while not self.Done:
            g.clock.tick(48)
            g.current_time = pg.time.get_ticks()
            self.handle_events()
            self.update_views()

    def handle_events(self):
        self.keys = []
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                self.keys.append(event.key)
            if event.type == pg.QUIT:
                self.Done = True
                return
        for key in self.keys:
            self.handle_key(key)

        pg.event.clear()

    def handle_key(self, key):
        km = g.key_mode()
        if km == c.KEY_MODE_MAP:  # 控制勇士在地图上移动
            if key == pg.K_ESCAPE:
                self.Done = True
            elif key == pg.K_UP:
                b.DIRECTION = c.D_UP
                self.handle_item((b.POS_R - 1, b.POS_C))
            elif key == pg.K_DOWN:
                b.DIRECTION = c.D_DOWN
                self.handle_item((b.POS_R + 1, b.POS_C))
            elif key == pg.K_LEFT:
                b.DIRECTION = c.D_LEFT
                self.handle_item((b.POS_R, b.POS_C - 1))
            elif key == pg.K_RIGHT:
                b.DIRECTION = c.D_RIGHT
                self.handle_item((b.POS_R, b.POS_C + 1))
        elif km == c.KEY_MODE_SHOP:
            if key == pg.K_UP:
                g.dialogue_shop.move_up()
            elif key == pg.K_DOWN:
                g.dialogue_shop.move_down()
            elif key == pg.K_RETURN or key == pg.K_SPACE:
                g.dialogue_shop.confirm()

    @staticmethod
    def handle_item(pos): # 处理r行c列的物品
        row, col = pos
        cur_item = items.item_info[b.floorData[row][col]]
        if cur_item.item_can_pass:
            b.POS_R, b.POS_C = pos
        result = cur_item.touched()
        if result:  # 该物品即将消失
            b.floorData[row][col] = c.GROUND

    @staticmethod
    def update_views():   # 渲染视图
        g.screen.fill([35, 35, 35])

        for row in range(13):
            for col in range(13):
                g.vm.draw_by_rel_pos(g.screen, c.GROUND, (col, row)) # 画13*13网格

        for row in range(13):
            for col in range(13):
                g.vm.draw_by_rel_pos(g.screen, b.floorData[row][col], (col, row)) # 画13*13网格

        g.vm.draw_by_rel_pos(g.screen, c.BRAVER, (b.POS_C, b.POS_R), index=b.DIRECTION * 4)  # 画勇者
        g.vm.print_attributes(g.screen)

        if b.SHOW_DAMAGE:
            g.vm.show_damages(g.screen)

        g.dialogue_shop.print(g.screen)
        g.vm.update_index()

        pg.display.update()


# 1 绘制背景*
# 2 接受event
# 3 添加自然的动画
# 4 添加勇者
# 5 实现勇者的运动
# 6 判断墙壁的可通行性
# 7 显示人物属性
# 8 添加钥匙,血瓶,宝石
# 9 添加门
# 10 添加多层楼和楼梯
# 11 引入怪物和战斗机制
# 12 显伤
# 13 做0,1,2,3层塔的内容
# 14 商店购买机制
