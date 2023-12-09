from player import player

class Cutscenes :
    def __init__(self) :
        self.obj = None
        self.upcoming = []
        self.num = 0

class Cam :
    def __init__(self) :
        self.pos = [ 0, 0 ]
        self.pPos = [ 0, 0 ]
        self.minPos = [ 570, -80 ]
        self.maxPos = [ 2970, 1520 ]

class UI :
    def __init__(self) :
        self.mode = 'loading'
        
        self.paused = False
        self.pmTab = 0
        self.pmTabs = []
        
        self.images = []
        self.buttons = []
        
        self.scanner = False
        
        self.shop = None
        self.shopSelected = 0
        self.lastBoughtItem = None
        
        self.shake = 0
        self.game_over = -1
        
        self.transit = 0
        self.transitTo = 0
        self.transitPos = None
    
        self.width_static = 600
        self.height_static = 400
        
        self.cutscene = Cutscene()
    
    def has_focus(self) :
        return !self.paused and !self.cutscene.obj and self.transit <= 0 and self.game_over < 0
    
    def should_draw_overlay(self) :
        return self.paused or (player.itemInUse and player.itemInUse.throwable())

class Controls :
    def __init__(self) :
        self.dPressed = False # Pun not intended.
        self.aPressed = False
    
        self.debug1Pressed = False
        self.debug2Pressed = False
