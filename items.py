import constants as c
import gameAttributes as b
from monsterData import monster_data
import general as g


class Item:
    def __init__(self, item_id, item_type, can_pass):
        self.item_id = item_id
        self.item_type = item_type
        self.item_can_pass = can_pass

    def touched(self):
        return False  # 返回True表示该物体触碰后会消失，False表示不会


class Resource(Item):
    def __init__(self, item_id, item_type, can_pass):
        Item.__init__(self, item_id, item_type, can_pass)

    def touched(self):
        if self.item_id == c.YELLOW_KEY:
            b.YELLOW_KEY += 1
            return True
        elif self.item_id == c.BLUE_KEY:
            b.BLUE_KEY += 1
            return True
        elif self.item_id == c.RED_KEY:
            b.RED_KEY += 1
            return True
        elif self.item_id == c.RED_BOTTLE:
            b.HP += c.RED_BOTTLE_RECOVERY
            return True
        elif self.item_id == c.BLUE_BOTTLE:
            b.HP += c.BLUE_BOTTLE_RECOVERY
            return True
        elif self.item_id == c.RED_GEM:
            b.ATK += c.RED_GEM_ADD
            return True
        elif self.item_id == c.BLUE_GEM:
            b.DEF += c.BLUE_GEM_ADD
            return True
        elif self.item_id == c.YELLOW_GATE:
            if b.YELLOW_KEY > 0:
                b.YELLOW_KEY -= 1
                return True
            else:
                return False
        elif self.item_id == c.BLUE_GATE:
            if b.BLUE_KEY > 0:
                b.BLUE_KEY -= 1
                return True
            else:
                return False
        elif self.item_id == c.RED_GATE:
            if b.RED_KEY > 0:
                b.RED_KEY -= 1
                return True
            else:
                return False
        elif self.item_id == c.STEEL_GATE:
            return True


class Teleport(Item):
    def __init__(self, item_id, item_type, can_pass):
        Item.__init__(self, item_id, item_type, can_pass)

    def touched(self):
        if self.item_id == c.STAIRS_UP:
            b.change_floor(b.CURRENT_FLOOR+1)
        elif self.item_id == c.STAIRS_DOWN:
            b.change_floor(b.CURRENT_FLOOR-1)
        return False


class Monster(Item):
    def __init__(self, item_id, item_type, can_pass):
        Item.__init__(self, item_id, item_type, can_pass)

    def calc_damage(self): # 返回值，赢了True，输了False，下一个参数是预计损伤
        m_HP, m_ATK, m_DEF, m_GLD, m_EXP, m_AGI, m_SKILLS = monster_data[self.item_id]
        HP, ATK, DEF, AGI = b.HP, b.ATK, b.DEF, b.AGI
        total_damage_m2b = 0

        MAGIC = c.SKILL_MAGIC in m_SKILLS
        DOUBLE_ATTACK = c.SKILL_DOUBLE_ATTACK in m_SKILLS
        TRIPLE_ATTACK = c.SKILL_DOUBLE_ATTACK in m_SKILLS

        while True:
            # 勇士先攻击
            damage_b2m = ATK - m_DEF if ATK > m_DEF else 0
            if damage_b2m == 0:
                return False, 99999999
            m_HP -= damage_b2m
            if m_HP <= 0:
                break
            # 怪物攻击
            per_damage_m2b = (m_ATK - DEF if m_ATK > DEF else 0) if not MAGIC else m_ATK
            if DOUBLE_ATTACK:
                per_damage_m2b *= 2
            elif TRIPLE_ATTACK:
                per_damage_m2b *= 3
            total_damage_m2b += per_damage_m2b

        # total_damage_m2b = int(total_damage_m2b/(1-m_AGI/100))
        if total_damage_m2b < HP:
            return True, total_damage_m2b
        else:
            return False, total_damage_m2b

    def touched(self):    # combat...
        m_HP, m_ATK, m_DEF, m_GLD, m_EXP, m_AGI, m_SKILLS = monster_data[self.item_id]
        braver_win, damage = self.calc_damage()
        if braver_win:
            print('损失体力=', damage)
            b.HP -= damage
            b.GOLD += m_GLD
            b.EXP += m_EXP
        else:
            print('不可战胜该怪')
        return braver_win


class Npc(Item):
    def __init__(self, item_id, item_type, can_pass):
        Item.__init__(self, item_id, item_type, can_pass)

    def touched(self):
        if self.item_id == c.SHOP:
            g.dialogue_shop.show()
        return False


item_info = {c.GROUND: Item(c.GROUND, c.I_TERRAIN, can_pass=True),
             c.E_WALL: Item(c.E_WALL, c.I_TERRAIN, can_pass=False),
             c.WALL_WHITE: Item(c.E_WALL, c.I_TERRAIN, can_pass=False),
             c.WALL_BROWN: Item(c.WALL_BROWN, c.I_TERRAIN, can_pass=False),
             c.LAVA: Item(c.LAVA, c.I_TERRAIN, can_pass=False),

             c.STAIRS_UP: Teleport(c.STAIRS_UP, c.I_TELEPORT, can_pass=True),
             c.STAIRS_DOWN: Teleport(c.STAIRS_DOWN, c.I_TELEPORT, can_pass=True),

             c.YELLOW_KEY: Resource(c.YELLOW_KEY, c.I_RESOURCE, can_pass=False),
             c.BLUE_KEY: Resource(c.BLUE_KEY, c.I_RESOURCE, can_pass=False),
             c.RED_KEY: Resource(c.RED_KEY, c.I_RESOURCE, can_pass=False),
             c.RED_BOTTLE: Resource(c.RED_BOTTLE, c.I_RESOURCE, can_pass=False),
             c.BLUE_BOTTLE: Resource(c.BLUE_BOTTLE, c.I_RESOURCE, can_pass=False),
             c.RED_GEM: Resource(c.RED_GEM, c.I_RESOURCE, can_pass=False),
             c.BLUE_GEM: Resource(c.BLUE_GEM, c.I_RESOURCE, can_pass=False),
             c.YELLOW_GATE: Resource(c.YELLOW_GATE, c.I_RESOURCE, can_pass=False),
             c.BLUE_GATE: Resource(c.BLUE_GATE, c.I_RESOURCE, can_pass=False),
             c.RED_GATE: Resource(c.RED_GATE, c.I_RESOURCE, can_pass=False),
             c.STEEL_GATE: Resource(c.STEEL_GATE, c.I_RESOURCE, can_pass=False),

             c.SHOP_LEFT:  Item(c.SHOP_LEFT, c.I_TERRAIN, can_pass=False),
             c.SHOP_RIGHT: Item(c.SHOP_RIGHT, c.I_TERRAIN, can_pass=False),
             c.SHOP:       Npc(c.SHOP, c.I_NPC, can_pass=False)
             }

for item_id in range(c.M_SLIME, c.M_SLIME+50):  # 这些是预置的怪物
    item_info[item_id] = Monster(item_id, c.I_MONSTER, can_pass=False)