class World :
    def __init__(self) :
        self.collision_boxes = []
        self.blocks = [ [], [] ]
        self.land_shapes = []
        self.doors = []
        self.locked_doors = []
        self.save_block = None
        self.entities = []
        self.clouds = []
        self.explosions = []
