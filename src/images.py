import graphics as g
from enum import StrEnum

abl_img_path = 'res/inventory/abilities'
class Abilities(StrEnum) :
    lamp    = auto()
    lantern = auto()
    scanner = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, g.graphics.dir_images(self, abl_img_path + self))

class BG(StrEnum) :
    hills_trees = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, { self: g.GraphicsImage(self, self, bg_func[self], 3200, 400) }) 

    @property
    def image(self) :
        return self.images[self]

block_img_path = 'res/blocks'
class Blocks(StrEnum) :
    bricks          = auto()
    dirt            = auto()
    door            = auto()
    door_fireplace  = auto()
    door_glass      = auto()
    door_save       = auto()
    door_smoke      = auto()
    glass           = auto()
    grass           = auto()
    iron_grate      = auto()
    leaves_beech    = auto()
    leaves_hedge    = auto()
    log_beech       = auto()
    planks          = auto()
    sand            = auto()
    sandstone       = auto()
    stone           = auto()
    stone_bricks    = auto()
    waterfall       = auto()
    window          = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, g.graphics.dir_images(self, block_img_path + self))

char_img_path = 'res/char'
class Characters(StrEnum) :
    clockwork_soldier   = auto()
    elram               = auto()
    guard               = auto()
    jester              = auto()
    lamp                = auto()
    marle               = auto()
    prof_schlierich     = auto()
    ribbamech           = auto()
    scarab              = auto()
    tamul               = auto()
    town1               = auto()
    town2               = auto()
    town3               = auto()
    town4               = auto()
    town5               = auto()
    town6               = auto()
    town_shopkeeper     = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, g.graphics.dir_images(self, char_img_path + self)) 

deco_img_path = 'res/deco'
class Decoration(StrEnum) :
    cloud   = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, g.graphics.dir_images(self, deco_img_path + self)) 

equip_img_path = 'res/inventory/equipment'
class Equipment(StrEnum) :
    battleaxe       = auto()
    dagger_curved   = auto()
    hammer          = auto() 
    scimitar        = auto()
    spear           = auto()
    spear_stone     = auto()
    stick           = auto()
    sword           = auto()
    sword2          = auto()
    sword3          = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, g.graphics.dir_images(self, equip_img_path + self)) 

item_img_path = 'res/inventory/items'
class Items(StrEnum) :
    apple           = auto()
    bread           = auto()
    cherry_bomb     = auto()
    cog_shield      = auto()
    elixir          = auto()
    key_dungeon     = auto()
    monkey_wrench   = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, g.graphics.dir_images(self, item_img_path + self)) 

fx_img_path = 'res/fx'
class FX(StrEnum) :
    attack_sweep        = auto()
    cog_shield          = auto()
    disappear_char      = auto()
    disappear_fire      = auto()
    disappear_ice       = auto()
    disappear_smoke     = auto()
    disappear_whirlwind = auto()
    elixir              = auto()
    explode             = auto()
    hurt_hostile        = auto()
    hurt_player         = auto()
    interact_hint       = auto()
    ribbamech_flame     = auto()
        
    @property
    def images(self) :
        return g.graphics.images.get(self, g.graphics.dir_images(self, fx_img_path + self)) 

ui_img_path = 'res/ui'
class UI(StrEnum) :
    dark                = auto()
    parttransitionbox   = auto()

    @property
    def images(self) :
        return g.graphics.images.get(self, { self: g.LoadedImage(self, self, ui_img_path + self + '.png') }) 

    @property
    def image(self) :
        return self.images[self]

bg_func = { BG.hills_trees: bg_hills_trees }

def bg_hills_trees(gObj) :
    gObj.background(220, 255, 255)
    for i in range(400) :
        gObj.stroke(lerpColor(color(220, 255, 255), color(150, 220, 220), i/400))
        gObj.line(0, i, 3000, i)
    
    gObj.noStroke()
    gObj.fill(61, 120, 46)
    gObj.bezier(-30, 400, 100, 200, 500, 190, 640, 400)
    for i in range(0, 200, 2) :
        gObj.fill(0, 120 - (i/3), 46 - (i/12))
        gObj.bezier(-30, 400, 100, 200 + i/4, 500 - (i), 190 + i, 640 - i, 400)
    
    gObj.fill(54, 99, 41)
    gObj.bezier((800), 400, (900), 180, (2000), 200, (2900), 400)
    for i in range(0, 200, 2) :
        gObj.fill(54 - (i/4), 99 - (i/3), 41 - (i/12))
        gObj.bezier(800 + (i/8), 400, 900 + i/4, 180 + i/2, 2000 - (i), 200 + i, 2900 - i*10, 400)
    
    gObj.fill(73, 148, 52)
    gObj.bezier((550), 400, (700), 100, (800), 150, (1072), 400)
    for i in range(0, 200, 2) :
        gObj.fill(73 - (i/4), 148 - (i/3), 52 - (i/12))
        gObj.bezier(550, 400, 700, 100 + i, 800 - (i), 150 + i*1.5, 1072 - i, 400)
    
    # Hill 1
    drawTree(gObj, 100, 265, 3)
    drawTree(gObj, 200, 255, 2)
    drawTree(gObj, 130, 252, 2)
    drawTree(gObj, 80, 290, 2)
    drawTree(gObj, 30, 295, 3)
    drawTree(gObj, 140, 265, 2)
    drawTree(gObj, 220, 260, 3)
    drawTree(gObj, 250, 235, 3)
    drawTree(gObj, 260, 265, 2)
    drawTree(gObj, 310, 240, 2)
    drawTree(gObj, 330, 260, 3)
    drawTree(gObj, 370, 225, 3)
    drawTree(gObj, 420, 235, 3)
    drawTree(gObj, 450, 265, 2)
    drawTree(gObj, 470, 260, 3)
    drawTree(gObj, 510, 285, 2)

    # Hill 2
    drawTree(gObj, 590, 285, 2)
    drawTree(gObj, 625, 245, 3)
    drawTree(gObj, 645, 265, 3)
    drawTree(gObj, 630, 235, 2)
    drawTree(gObj, 640, 255, 3)
    drawTree(gObj, 670, 225, 2)
    drawTree(gObj, 655, 235, 2)
    drawTree(gObj, 685, 255, 2)
    drawTree(gObj, 700, 215, 2)
    drawTree(gObj, 725, 225, 3)
    drawTree(gObj, 740, 235, 3)
    drawTree(gObj, 770, 255, 3)
    drawTree(gObj, 780, 205, 2)
    drawTree(gObj, 755, 185, 2)
    drawTree(gObj, 805, 195, 3)
    drawTree(gObj, 830, 175, 4)
    drawTree(gObj, 845, 180, 2)
    drawTree(gObj, 850, 195, 2)
    drawTree(gObj, 860, 220, 3)
    drawTree(gObj, 890, 205, 3)
    drawTree(gObj, 825, 225, 2)
    drawTree(gObj, 900, 235, 2)
    drawTree(gObj, 925, 245, 2)
    drawTree(gObj, 935, 235, 2)

    # Hill 3
    drawTree(gObj, 1000, 265, 3)
    drawTree(gObj, 1200, 235, 2)
    drawTree(gObj, 1130, 232, 2)
    drawTree(gObj, 1080, 250, 2)
    drawTree(gObj, 1030, 265, 3)
    drawTree(gObj, 1140, 285, 2)
    drawTree(gObj, 1220, 240, 3)
    drawTree(gObj, 1250, 215, 3)
    drawTree(gObj, 1260, 225, 2)
    drawTree(gObj, 1310, 200, 2)
    drawTree(gObj, 1330, 250, 3)
    drawTree(gObj, 1370, 205, 3)
    drawTree(gObj, 1420, 195, 3)
    drawTree(gObj, 1450, 245, 2)
    drawTree(gObj, 1470, 220, 3)
    drawTree(gObj, 1510, 255, 2)
    drawTree(gObj, 1020, 285, 3)
    drawTree(gObj, 1210, 245, 2)
    drawTree(gObj, 1115, 239, 2)
    drawTree(gObj, 1070, 280, 2)
    drawTree(gObj, 1050, 275, 3)
    drawTree(gObj, 1130, 300, 2)
    drawTree(gObj, 1230, 250, 3)
    drawTree(gObj, 1265, 225, 3)
    drawTree(gObj, 1270, 255, 2)
    drawTree(gObj, 1300, 220, 2)
    drawTree(gObj, 1315, 240, 3)
    drawTree(gObj, 1390, 225, 3)
    drawTree(gObj, 1415, 310, 3)
    drawTree(gObj, 1460, 235, 2)
    drawTree(gObj, 1490, 240, 3)
    drawTree(gObj, 1480, 275, 2)

    bgHillsTreesRaw = gObj.get()
    gObj.image(bgHillsTreesRaw, 0, 0)
    gObj.filter(BLUR, 3)

def draw_tree(g, x, y, t) :
    g.fill(87, 54, 24)
    g.rect(x - 5, y + (t * 10), 10, 30)
    g.fill(0, 97, 0)
    
    for i in range(t) :
        g.triangle(x - 15, y + 10 + (i * 15), x + 15, y + 10 + (i * 15), x, y - 15 + (i * 15))
