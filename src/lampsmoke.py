from graphics import graphics

tick = 0
saveFile = None
curr_level = None
DEBUG = False

def debug(msg) :
    if DEBUG : print(msg)

def setup() :
    size(1200, 800)
    frameRate(24)
    debug("Loading Images")
    graphics.load_images()
