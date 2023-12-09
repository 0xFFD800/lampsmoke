class Graphics :
    def __init__(self) :
        self.images = []

    def load_graphics(self) :
        pass

graphics = Graphics()

class Image :
    def __init__(self) :
        img = None

class LoadedImage(Image) :
    def __init__(self, f) :
        Image.__init__(self)
        self.file = f
        graphics.images.append(self)

    def load(self) :
        self.img = loadImage(self.file)

class GraphicsImage(Image) :
    def __init__(self, dF, sX, sY) :
        Image.__init__(self)
        self.draw_func = dF
        self.size_x = sX
        self.size_y = sY
        graphics.images.append(self)

    def load(self) :
        gObj = createGraphics(self.size_x, self.size_y, JAVA2D)
        self.draw_func(gObj)
        self.img = gObj.get()

def draw_tree(g, x, y, t) :
    g.fill(87, 54, 24)
    g.rect(x - 5, y + (t * 10), 10, 30)
    g.fill(0, 97, 0)
    
    for i in range(t) :
        g.triangle(x - 15, y + 10 + (i * 15), x + 15, y + 10 + (i * 15), x, y - 15 + (i * 15))
