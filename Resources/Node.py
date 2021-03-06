class Node:

    def __init__(self, State, StateN, Pos, Level):
        self.State = State
        self.StateN = StateN
        self.Weight = [[], []]
        self.Time = [[], []]
        self.MT = None
        self.Pos = Pos
        self.Adj = []
        self.Level = Level
        self.Visited = False
        self.Accept = False
        self.x = 0
        self.y = 0
        self.Father = None
        self.Min = [0, None]
        self.Image = None
        self.ImageP = [0, 0]
        self.ImageG = 0

    def __eq__(self, node):
        exist = False
        for i in range(len(self.State)):
            for j in range(len(self.State[i])):
                if self.State[i][j] == node.State[i][j]:
                    exist = True
                else:
                    exist = False
                    break

        if self.MT != None:
            if self.MT != node.MT:
                return False

        return (exist and self.Pos is node.Pos)
