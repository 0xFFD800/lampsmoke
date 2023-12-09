from player import player

class Cutscenes :
    obj = None
    upcoming = []
    num = 0

class Cam :
    pos = [ 0, 0 ]
    pPos = [ 0, 0 ]
    minPos = [ 570, -80 ]
    maxPos = [ 2970, 1520 ]

class UI :
    mode = 'loading'

    paused = False
    pmTab = 0
    pmTabs = []
    
    images = []
    buttons = []
    
    scanner = False
    
    shop = None
    shopSelected = 0
    lastBoughtItem = None
    
    shake = 0
    game_over = -1
    
    transit = 0
    transitTo = 0
    transitPos = None

    width_static = 600
    height_static = 400
    
    cutscene = Cutscene()
    
    def has_focus() :
        return !paused and !cutscene.obj and transit <= 0 and game_over < 0
    
    def should_draw_overlay() :
        return paused or (player.itemInUse and player.itemInUse.throwable())
