from Resources.Node import Node
from Resources.Edge import Edge
from random import randint
from math import inf


class CrossRiver:

    def __init__(self):
        self.Alphabet = ['L1', 'L2', 'R1', 'R2']
        self.Nodes = []
        self.Edges = []
        self.Root = None
        self.MaxWeight = 0
        self.MinWaysL = []
        self.Min = []
        self.NoDrive = []
        self.NoDriveWith = []
        self.NoAloneTog = []
        self.NoMore = []
        self.Guard = []
        self.NotAlone = []
        self.DriveAlone = []
        self.constraintZ = []
        self.constraintO = []
        self.StateInit = [[], []]
        self.StateInitN = [[], []]
        self.EWeight = [[], []]
        self.StateAccept = [[], []]

    def Start(self):
        min = inf
        for entity in self.StateInit[0]:
            self.StateInit[1].append('')
            if len(self.StateInitN[0]) > 0:
                self.StateInitN[1].append(0)
        self.StateAccept[0] = self.StateInit[1]
        self.StateAccept[1] = self.StateInit[0]
        if len(self.StateInitN[0]) > 0:
            self.Root = Node(self.StateInit, self.StateInitN, 'L', 1)
        else:
            self.Root = Node(self.StateInit, [[], []], 'L', 1)
        self.Nodes.append(self.Root)
        self.Root = self.GenerateTransitions(self.Root)
        self.CreateEdge()
        self.MinWays(self.Root, [])
        if len(self.Nodes) < 30:
            self.Root = self.SetPositions(self.Root)
        else:
            for list in self.MinWaysL:
                self.setPosMin(list)
        for Mlist in self.MinWaysL:
            if len(Mlist) < min:
                min = len(Mlist)
                self.Min = Mlist
        # self.show()
        return self

    def GenerateTransitions(self, Father):
        cant = 0
        for transition in self.Alphabet:
            if transition[0] != Father.Pos:
                if len(Father.StateN[1]) == 1:
                    cant = Father.StateN[1][0]
                if transition is 'L1':
                    if len(Father.State[1]) >= 1 or cant >= 1:
                        for i in range(len(Father.State[1])):
                            dig = True
                            DigT = ''
                            NDig = ''
                            pw = True
                            for c in range(len(Father.State[1][i])):
                                if Father.State[1][i][c].isdigit() and dig:
                                    DigT = DigT + Father.State[1][i][c]
                                else:
                                    NDig = NDig + Father.State[1][i][c]
                                    dig = False

                            if self.MaxWeight > 0:
                                if self.EWeight[i] < self.MaxWeight:
                                    pw = True
                                else:
                                    pw = False

                            if (Father.State[1][i] != '' and NDig not in self.NoDrive
                                    and NDig not in self.NotAlone and pw):
                                exist = True
                                dig = True
                                DigT = ''
                                NDig = ''
                                temp = Node([[], []], [[], []],
                                            'L', Father.Level + 1)
                                temp.Father = Father

                                for a in range(len(Father.StateN)):
                                    for b in range(len(Father.StateN[a])):
                                        temp.StateN[a].append(
                                            Father.StateN[a][b])

                                for j in range(len(Father.State)):
                                    for k in range(len(Father.State[j])):
                                        temp.State[j].append(
                                            Father.State[j][k])

                                for c in range(len(temp.State[1][i])):
                                    if temp.State[1][i][c].isdigit() and dig:
                                        DigT = DigT + temp.State[1][i][c]
                                    else:
                                        NDig = NDig + temp.State[1][i][c]
                                        dig = False

                                if DigT != '':
                                    temp.StateN[0][i] += 1
                                    temp.StateN[1][i] -= 1
                                    temp.State[0][i] = f"{temp.StateN[0][i]}{NDig}"
                                    if temp.StateN[1][i] > 0:
                                        temp.State[1][i] = f"{temp.StateN[1][i]}{NDig}"
                                    else:
                                        temp.StateN[1][i] = 0
                                        temp.State[1][i] = ''
                                else:
                                    temp.State[0][i] = Father.State[1][i]
                                    temp.State[1][i] = ''

                                if not self.Constraints(temp):
                                    continue

                                for node in self.Nodes:
                                    if temp == node:
                                        exist = False
                                        for n in Father.Adj:
                                            if node == n:
                                                exist = True
                                            else:
                                                exist = False
                                        if not exist:
                                            Father.Adj.append(node)
                                            exist = True
                                        break
                                    else:
                                        exist = False

                                if not exist:
                                    self.Nodes.append(temp)
                                    Father.Adj.append(temp)

                if transition is 'L2':
                    if len(Father.StateN[1]) == 1:
                        cant = Father.StateN[1][0]
                    if len(Father.State[1]) >= 2 or cant >= 2:
                        for i in range(len(Father.State[1])):
                            dig = True
                            DigT = ''
                            NDig = ''
                            pw = True
                            for c in range(len(Father.State[1][i])):
                                if Father.State[1][i][c].isdigit() and dig:
                                    DigT = DigT + Father.State[1][i][c]
                                else:
                                    NDig = NDig + Father.State[1][i][c]
                                    dig = False

                            if self.MaxWeight > 0:
                                if self.EWeight[i]*2 < self.MaxWeight:
                                    pw = True
                                else:
                                    pw = False

                            if (Father.StateN[1][i] >= 2 and NDig not in self.DriveAlone
                                    and NDig not in self.NoDrive and pw):
                                dig = True
                                exist = True
                                DigT = ''
                                NDig = ''
                                temp = Node([[], []], [[], []],
                                            'L', Father.Level + 1)
                                temp.Father = Father

                                for a in range(len(Father.StateN)):
                                    for b in range(len(Father.StateN[a])):
                                        temp.StateN[a].append(
                                            Father.StateN[a][b])

                                for k in range(len(Father.State)):
                                    for l in range(len(Father.State[k])):
                                        temp.State[k].append(
                                            Father.State[k][l])

                                for c in range(len(temp.State[1][i])):
                                    if temp.State[1][i][c].isdigit() and dig:
                                        DigT = DigT + temp.State[1][i][c]
                                    else:
                                        NDig = NDig + temp.State[1][i][c]
                                        dig = False
                                dig = True

                                temp.StateN[0][i] += 2
                                temp.StateN[1][i] -= 2
                                temp.State[0][i] = f"{temp.StateN[0][i]}{NDig}"
                                if temp.StateN[1][i] > 0:
                                    temp.State[1][i] = f"{temp.StateN[1][i]}{NDig}"
                                else:
                                    temp.StateN[1][i] = 0
                                    temp.State[1][i] = ''

                                if self.Constraints(temp):
                                    for node in self.Nodes:
                                        if temp == node:
                                            exist = False
                                            for n in Father.Adj:
                                                if node == n:
                                                    exist = True
                                                else:
                                                    exist = False
                                            if not exist:
                                                Father.Adj.append(node)
                                                exist = True
                                            break
                                        else:
                                            exist = False

                                    if not exist:
                                        self.Nodes.append(temp)
                                        Father.Adj.append(temp)

                            for j in range(i+1, len(Father.State[1])):
                                if Father.State[1][i] != '' and Father.State[1][j] != '':
                                    exist = True
                                    dig = True
                                    NoDriveW = False
                                    DigT = ''
                                    DigTT = ''
                                    NDig = ''
                                    NDigT = ''
                                    pw = True
                                    temp = Node([[], []], [[], []],
                                                'L', Father.Level + 1)
                                    temp.Father = Father

                                    for a in range(len(Father.StateN)):
                                        for b in range(len(Father.StateN[a])):
                                            temp.StateN[a].append(
                                                Father.StateN[a][b])

                                    for k in range(len(Father.State)):
                                        for l in range(len(Father.State[k])):
                                            temp.State[k].append(
                                                Father.State[k][l])

                                    for c in range(len(temp.State[1][i])):
                                        if temp.State[1][i][c].isdigit() and dig:
                                            DigT = DigT + temp.State[1][i][c]
                                        else:
                                            NDig = NDig + temp.State[1][i][c]
                                            dig = False
                                    dig = True

                                    for d in range(len(temp.State[1][j])):
                                        if temp.State[1][j][d].isdigit() and dig:
                                            DigTT = DigTT + temp.State[1][j][d]
                                        else:
                                            NDigT = NDigT + temp.State[1][j][d]
                                            dig = False

                                    for list in self.NoDriveWith:
                                        if ((NDig == list[1] or NDig == list[0]) and
                                                (NDigT == list[0] or NDigT == list[1])):
                                            NoDriveW = True
                                            break
                                        else:
                                            NoDriveW = False

                                    if self.MaxWeight > 0:
                                       if (self.EWeight[i] + self.EWeight[j]) < self.MaxWeight:
                                           pw = True
                                       else:
                                           pw = False

                                    if (NDig in self.DriveAlone or NDigT in self.DriveAlone or
                                            (NDig in self.NoDrive and NDigT in self.NoDrive) or NoDriveW or not pw):
                                        continue

                                    if DigT != '':
                                        temp.StateN[0][i] += 1
                                        temp.StateN[1][i] -= 1
                                        temp.State[0][i] = f"{temp.StateN[0][i]}{NDig}"
                                        if temp.StateN[1][i] > 0:
                                            temp.State[1][i] = f"{temp.StateN[1][i]}{NDig}"
                                        else:
                                            temp.StateN[1][i] = 0
                                            temp.State[1][i] = ''
                                    else:
                                        temp.State[0][i] = Father.State[1][i]
                                        temp.State[1][i] = ''

                                    if DigTT != '':
                                        temp.StateN[0][j] += 1
                                        temp.StateN[1][j] -= 1
                                        temp.State[0][j] = f"{temp.StateN[0][j]}{NDigT}"
                                        if temp.StateN[1][j] > 0:
                                            temp.State[1][j] = f"{temp.StateN[1][j]}{NDigT}"
                                        else:
                                            temp.StateN[1][j] = 0
                                            temp.State[1][j] = ''
                                    else:
                                        temp.State[0][j] = Father.State[1][j]
                                        temp.State[1][j] = ''

                                    if not self.Constraints(temp):
                                        continue

                                    for node in self.Nodes:
                                        if temp == node:
                                            exist = False
                                            for n in Father.Adj:
                                                if node == n:
                                                    exist = True
                                                else:
                                                    exist = False
                                            if not exist:
                                                Father.Adj.append(node)
                                                exist = True
                                            break
                                        else:
                                            exist = False

                                    if not exist:
                                        self.Nodes.append(temp)
                                        Father.Adj.append(temp)

                if transition is 'R1':
                    if len(Father.StateN[0]) == 1:
                        cant = Father.StateN[0][0]
                    if len(Father.State[0]) >= 1 or cant >= 1:
                        for i in range(len(Father.State[0])):
                            dig = True
                            DigT = ''
                            NDig = ''
                            pw = True
                            for c in range(len(Father.State[0][i])):
                                if Father.State[0][i][c].isdigit() and dig:
                                    DigT = DigT + Father.State[0][i][c]
                                else:
                                    NDig = NDig + Father.State[0][i][c]
                                    dig = False
                            
                            if self.MaxWeight > 0:
                                if self.EWeight[i] < self.MaxWeight:
                                    pw = True
                                else:
                                    pw = False

                            if (Father.State[0][i] != '' and NDig not in self.NoDrive
                                    and NDig not in self.NotAlone):
                                exist = True
                                dig = True
                                DigT = ''
                                NDig = ''
                                temp = Node([[], []], [[], []], 'R', Father.Level + 1)
                                temp.Father = Father

                                for a in range(len(Father.StateN)):
                                    for b in range(len(Father.StateN[a])):
                                        temp.StateN[a].append(
                                            Father.StateN[a][b])

                                for j in range(len(Father.State)):
                                    for k in range(len(Father.State[j])):
                                        temp.State[j].append(
                                            Father.State[j][k])

                                for c in range(len(temp.State[0][i])):
                                    if temp.State[0][i][c].isdigit() and dig:
                                        DigT = DigT + temp.State[0][i][c]
                                    else:
                                        NDig = NDig + temp.State[0][i][c]
                                        dig = False

                                if DigT != '':
                                    temp.StateN[1][i] += 1
                                    temp.StateN[0][i] -= 1
                                    temp.State[1][i] = f"{temp.StateN[1][i]}{NDig}"
                                    if temp.StateN[0][i] > 0:
                                        temp.State[0][i] = f"{temp.StateN[0][i]}{NDig}"
                                    else:
                                        temp.StateN[0][i] = 0
                                        temp.State[0][i] = ''
                                else:
                                    temp.State[1][i] = Father.State[0][i]
                                    temp.State[0][i] = ''

                                if not self.Constraints(temp):
                                    continue

                                for node in self.Nodes:
                                    if temp == node:
                                        exist = False
                                        for n in Father.Adj:
                                            if node == n:
                                                exist = True
                                            else:
                                                exist = False
                                        if not exist:
                                            Father.Adj.append(node)
                                            exist = True
                                        break
                                    else:
                                        exist = False

                                if not exist:
                                    self.Nodes.append(temp)
                                    Father.Adj.append(temp)

                if transition is 'R2':
                    if len(Father.StateN[0]) == 1:
                        cant = Father.StateN[0][0]
                    if len(Father.State[0]) >= 2 or cant >= 2:
                        for i in range(len(Father.State[0])):
                            dig = True
                            DigT = ''
                            NDig = ''
                            pw = True
                            for c in range(len(Father.State[0][i])):
                                if Father.State[0][i][c].isdigit() and dig:
                                    DigT = DigT + Father.State[0][i][c]
                                else:
                                    NDig = NDig + Father.State[0][i][c]
                                    dig = False
                            
                            if self.MaxWeight > 0:
                                if self.EWeight[i]*2 < self.MaxWeight:
                                    pw = True
                                else:
                                    pw = False

                            if (Father.StateN[0][i] >= 2 and NDig not in self.DriveAlone and
                                    NDig not in self.NoDrive and pw):
                                dig = True
                                exist = True
                                DigT = ''
                                NDig = ''
                                temp = Node([[], []], [[], []], 'R', Father.Level + 1)
                                temp.Father = Father

                                for a in range(len(Father.StateN)):
                                    for b in range(len(Father.StateN[a])):
                                        temp.StateN[a].append(
                                            Father.StateN[a][b])

                                for k in range(len(Father.State)):
                                    for l in range(len(Father.State[k])):
                                        temp.State[k].append(
                                            Father.State[k][l])

                                for c in range(len(temp.State[0][i])):
                                    if temp.State[0][i][c].isdigit() and dig:
                                        DigT = DigT + temp.State[0][i][c]
                                    else:
                                        NDig = NDig + temp.State[0][i][c]
                                        dig = False
                                dig = True

                                temp.StateN[1][i] += 2
                                temp.StateN[0][i] -= 2
                                temp.State[1][i] = f"{temp.StateN[1][i]}{NDig}"
                                if temp.StateN[0][i] > 0:
                                    temp.State[0][i] = f"{temp.StateN[0][i]}{NDig}"
                                else:
                                    temp.StateN[0][i] = 0
                                    temp.State[0][i] = ''

                                if self.Constraints(temp):
                                    for node in self.Nodes:
                                        if temp == node:
                                            exist = False
                                            for n in Father.Adj:
                                                if node == n:
                                                    exist = True
                                                else:
                                                    exist = False
                                            if not exist:
                                                Father.Adj.append(node)
                                                exist = True
                                            break
                                        else:
                                            exist = False

                                    if not exist:
                                        self.Nodes.append(temp)
                                        Father.Adj.append(temp)

                            for j in range(i + 1, len(Father.State[0])):
                                if Father.State[0][i] != '' and Father.State[0][j] != '':
                                    exist = True
                                    dig = True
                                    NoDriveW = False
                                    NDig = ''
                                    NDigT = ''
                                    DigT = ''
                                    DigTT = ''
                                    pw = True
                                    temp = Node([[], []], [[], []], 'R', Father.Level + 1)
                                    temp.Father = Father

                                    for a in range(len(Father.StateN)):
                                        for b in range(len(Father.StateN[a])):
                                            temp.StateN[a].append(
                                                Father.StateN[a][b])

                                    for k in range(len(Father.State)):
                                        for l in range(len(Father.State[k])):
                                            temp.State[k].append(
                                                Father.State[k][l])

                                    for c in range(len(temp.State[0][i])):
                                        if temp.State[0][i][c].isdigit() and dig:
                                            DigT = DigT + temp.State[0][i][c]
                                        else:
                                            NDig = NDig + temp.State[0][i][c]
                                            dig = False
                                    dig = True

                                    for d in range(len(temp.State[0][j])):
                                        if temp.State[0][j][d].isdigit() and dig:
                                            DigTT = DigTT + temp.State[0][j][d]
                                        else:
                                            NDigT = NDigT + temp.State[0][j][d]
                                            dig = False

                                    for list in self.NoDriveWith:
                                        if ((NDig == list[1] or NDig == list[0]) and
                                                (NDigT == list[0] or NDigT == list[1])):
                                            NoDriveW = True
                                            break
                                        else:
                                            NoDriveW = False
                                    
                                    if self.MaxWeight > 0:
                                        if (self.EWeight[i] + self.EWeight[j]) < self.MaxWeight:
                                            pw = True
                                        else:
                                            pw = False

                                    if (NDig in self.DriveAlone or NDigT in self.DriveAlone or
                                            (NDig in self.NoDrive and NDigT in self.NoDrive) or NoDriveW or not pw):
                                        continue

                                    if DigT != '':
                                        temp.StateN[1][i] += 1
                                        temp.StateN[0][i] -= 1
                                        temp.State[1][i] = f"{temp.StateN[1][i]}{NDig}"
                                        if temp.StateN[0][i] > 0:
                                            temp.State[0][i] = f"{temp.StateN[0][i]}{NDig}"
                                        else:
                                            temp.StateN[0][i] = 0
                                            temp.State[0][i] = ''
                                    else:
                                        temp.State[1][i] = Father.State[0][i]
                                        temp.State[0][i] = ''

                                    if DigTT != '':
                                        temp.StateN[1][j] += 1
                                        temp.StateN[0][j] -= 1
                                        temp.State[1][j] = f"{temp.StateN[1][j]}{NDigT}"
                                        if temp.StateN[0][j] > 0:
                                            temp.State[0][j] = f"{temp.StateN[0][j]}{NDigT}"
                                        else:
                                            temp.StateN[0][j] = 0
                                            temp.State[0][j] = ''
                                    else:
                                        temp.State[1][j] = Father.State[0][j]
                                        temp.State[0][j] = ''

                                    if not self.Constraints(temp):
                                        continue

                                    for node in self.Nodes:
                                        if temp == node:
                                            exist = False
                                            for n in Father.Adj:
                                                if node == n:
                                                    exist = True
                                                else:
                                                    exist = False
                                            if not exist:
                                                Father.Adj.append(node)
                                                exist = True
                                            break
                                        else:
                                            exist = False

                                    if not exist:
                                        self.Nodes.append(temp)
                                        Father.Adj.append(temp)

        Father.Visited = True
        for i in range(len(Father.Adj)):
            if not Father.Adj[i].Visited:
                Father.Adj[i] = self.GenerateTransitions(Father.Adj[i])
        return Father

    def Constraints(self, temp):
        self.constraintZ = []
        self.constraintO = []
        MoreT = False
        Alone = True
        GuardZ = True
        GuardO = True
        VerConsZ = False
        VerConsO = False
        ConsZ = []
        ConsO = []
        Create = True
        dig = True
        dig2 = True
        DigT = ''
        NDig = ''
        Etemp = ''
        Edig = ''
        E1 = 0
        E2 = 0
        al = 0
        i = 0
        j = 0

        for a in range(len(self.NoAloneTog)):
            self.constraintZ.append([])
            self.constraintO.append([])
            for b in range(len(self.NoAloneTog[a])):
                self.constraintZ[a].append('')
                self.constraintO[a].append('')

        for ind in range(len(temp.State)):
            for c in range(len(temp.State[ind])):
                if temp.State[ind][c] != '':
                    NDig = ''
                    DigT = ''
                    dig = True
                    for x in range(len(temp.State[ind][c])):
                        if temp.State[ind][c][x].isdigit() and dig:
                            DigT = DigT + temp.State[ind][c][x]
                        else:
                            NDig = NDig + temp.State[ind][c][x]
                            dig = False
                    for d in range(len(self.NoAloneTog)):
                        for e in range(len(self.NoAloneTog[d])):
                            if NDig == self.NoAloneTog[d][e]:
                                if ind == 0:
                                    self.constraintZ[d][e] = NDig
                                else:
                                    self.constraintO[d][e] = NDig

        for f in range(len(self.constraintZ)):
            VerConsZ = False
            for g in range(len(self.constraintZ[f])):
                if self.constraintZ[f][g] == self.NoAloneTog[f][g]:
                    VerConsZ = True
                    i = f
                else:
                    VerConsZ = False
                    break
            if VerConsZ:
                ConsZ.append(i)

        if len(ConsZ) > 0:
            VerConsZ = True

        for f in range(len(self.constraintO)):
            VerConsO = False
            for g in range(len(self.constraintO[f])):
                if self.constraintO[f][g] == self.NoAloneTog[f][g]:
                    VerConsO = True
                    j = f
                else:
                    VerConsO = False
                    break
            if VerConsO:
                ConsO.append(j)

        if len(ConsO) > 0:
            VerConsO = True

        for s in range(len(self.NoMore)):
            for t in range(len(temp.State)):
                E1 = 0
                E2 = 0
                for u in range(len(temp.State[t])):
                    Etemp = ''
                    Edig = ''
                    dig2 = True
                    for char in temp.State[t][u]:
                        if char.isdigit() and dig2:
                            Edig = Edig + str(int(char) - 1)
                        else:
                            dig2 = False
                            Etemp = Etemp + char
                            if Etemp == self.NoMore[s][0]:
                                E1 += 1
                                if Edig != '':
                                    E1 += int(Edig)
                            elif Etemp == self.NoMore[s][1]:
                                E2 += 1
                                if Edig != '':
                                    E2 += int(Edig)
                if E1 != 0 and E2 != 0 and E1 > E2:
                    MoreT = True
                    break
            if MoreT:
                break

        for l in range(len(temp.State)):
            if l > 0 and Alone:
                break
            elif not Alone:
                Alone = True
                al = 0
            for m in range(len(temp.State[l])):
                if temp.State[l][m] in self.NotAlone and Alone:
                    Alone = True
                elif temp.State[l][m] != '':
                    Alone = False
                elif Alone:
                    al += 1
                    Alone = True
                    if al == len(temp.State[l]):
                        Alone = False

        if VerConsZ:
            for index in ConsZ:
                for p in range(len(temp.State[0])):
                    for n in range(len(self.Guard[index])):
                        if temp.State[0][p] == self.Guard[index][n]:
                            GuardZ = True
                            break
                        else:
                            GuardZ = False
                    if GuardZ:
                        break
                if not GuardZ:
                    break

        if VerConsO:
            for index in ConsO:
                for p in range(len(temp.State[1])):
                    for n in range(len(self.Guard[index])):
                        if temp.State[1][p] == self.Guard[index][n]:
                            GuardO = True
                            break
                        else:
                            GuardO = False
                    if GuardO:
                        break
                if not GuardZ:
                    break

        if ((VerConsZ and not GuardZ) or (VerConsO and not GuardO)) or Alone or MoreT:
            Create = False
        else:
            Create = True

        return Create

    def show(self):
        for edge in self.Edges:
            print(
                f"{edge.Origin.State}, {edge.Origin.Pos} ------> {edge.Destiny.State}, {edge.Destiny.Pos}")

    def CreateEdge(self):
        for Node in self.Nodes:
            for State in self.StateAccept:
                if self.VerifState(Node.State):
                    Node.Accept = True
            for Child in Node.Adj:
                E = Edge(Node, Child)
                self.Edges.append(E)

    def VerifState(self, State):
        for i in range(len(self.StateAccept)):
            for j in range(len(self.StateAccept[i])):
                if self.StateAccept[i][j] != State[i][j]:
                    return False
        return True

    def SetPositions(self, Father):
        if (Father.x and Father.y) != 0:
            return Father

        pas = False

        while not pas:
            x = randint(30, 1300)
            y = randint(20, 700)

            if Father == self.Root:
                pas = True
            else:
                for node in self.Nodes:
                    if ((node.x >= x + 15 or node.x <= x - 15)
                            and (node.y >= y + 15 or node.y <= y - 15)):
                        pas = True
                    else:
                        pas = False
                        break

            if pas:
                Father.x = x
                Father.y = y

        for i in range(len(Father.Adj)):
            Father.Adj[i] = self.SetPositions(Father.Adj[i])
        return Father

    def setPosMin(self, Min):
        for ent in Min:
            pas = False
            if ent.x == ent.y == 0:
                while not pas:
                    x = randint(30, 1300)
                    y = randint(20, 700)

                    if ent == self.Root:
                        pas = True
                    else:
                        for node in self.Nodes:
                            if ((node.x >= x + 15 or node.x <= x - 15)
                                    and (node.y >= y + 15 or node.y <= y - 15)):
                                pas = True
                            else:
                                pas = False
                                break

                    if pas:
                        ent.x = x
                        ent.y = y
    
    def MinWays(self, Father, min):
        act = []

        if Father.Accept:
            min.append(Father)
            self.MinWaysL.append([])
            for i in range(len(self.MinWaysL)):
                if len(self.MinWaysL[i]) == 0:
                    for enti in min:
                        self.MinWaysL[i].append(enti)
                    break
            return
        
        min.append(Father)
        for ent in min:
            act.append(ent)

        for Adj in Father.Adj:
            if Adj.Level > Father.Level:
                self.MinWays(Adj, min)
                min.clear()
                for ant in act:
                    min.append(ant)
        return

