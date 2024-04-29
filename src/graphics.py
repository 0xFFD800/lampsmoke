import os

class Graphics :
    def __init__(self) :
        self.images = dict()

    def load_graphics(self) :
        for group in self.images.values() :
            for img in group.values() :
                img.load()

    def dir_images(self, group, path) :
        imgs = dict()
        for filename in os.listdir(path) :
            name, ext = filename.split('.')
            imgs[name] = LoadedImage(name, group, path + '/' + filename)
        return imgs


graphics = Graphics()

class Image :
    def __init__(self) :
        self.img = None

    def load(self) :
        pass

class LoadedImage(Image) :
    def __init__(self, n, g, f) :
        Image.__init__(self)
        self.name = n
        self.group = g
        self.file = f
        imggroup = graphics.images.setdefault(g, dict())
        imggroup[n] = self

    def load(self) :
        Image.load(self)
        self.img = loadImage(self.file)

class GraphicsImage(Image) :
    def __init__(self, n, g, dF, sX, sY) :
        Image.__init__(self)
        self.name = n
        self.group = g
        self.draw_func = dF
        self.size_x = sX
        self.size_y = sY
        imggroup = graphics.images.setdefault(g, dict())
        imggroup[n] = self

    def load(self) :
        Image.load(self)
        gObj = createGraphics(self.size_x, self.size_y, JAVA2D)
        self.draw_func(gObj)
        self.img = gObj.get()
