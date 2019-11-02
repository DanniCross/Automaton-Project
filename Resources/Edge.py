class Edge:

    def __init__(self, Origin, Destiny):
        self.Origin = Origin
        self.Destiny = Destiny
        self.PosO = (self.Origin.x, self.Origin.y)
        self.PosD = (self.Destiny.x, self.Destiny.y)
