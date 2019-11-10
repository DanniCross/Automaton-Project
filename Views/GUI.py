import pygame
import sys
import subprocess
import tkinter
from tkinter import *
from Views.Button import Button as B
from Views.Cursor import Cursor
pygame.init()


class GUI:

    def __init__(self, graph):
        self.Graph = graph
        self.start = False
        self.State = [[], []]
        self.draw()

    def screen_size(self):
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]), int(line.split()[9][:-1]))
        return size

    def draw(self):
        Screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption("Cross River")
        font = pygame.font.SysFont("Times New Roman", 10)

        Background = pygame.image.load("Img/Background.jpg")
        Background = pygame.transform.scale(Background, (self.screen_size()))

        ButtonUp = pygame.image.load("Img/ButtonUp.png")
        ButtonUp = pygame.transform.scale(ButtonUp, (150, 150))
        ButtonDown = pygame.image.load("Img/ButtonDown.png")
        ButtonDown = pygame.transform.scale(ButtonDown, (150, 150))
        PlayB = B(ButtonUp, ButtonDown, self.screen_size()
                  [0] / 2 - 75, self.screen_size()[1] / 2 - 58)
        play = font.render("", True, (0, 0, 0))

        cursor = Cursor()

        while True:
            for event in pygame.event.get():
                if event.type is pygame.MOUSEBUTTONDOWN:
                    if cursor.colliderect(PlayB.rect):
                        ScreenTK = Tk()
                        size = self.screen_size()
                        ScreenTK.geometry(
                            f"620x340+{int(size[0]/2) - 305}+{int(size[1]/2) - 170}")
                        ScreenTK.title("Configure the automaton")
                        ScreenTK.resizable(0, 0)
                        Entity = StringVar()
                        EntitiesT = StringVar(
                            value=f"{self.Graph.StateInit[0]}")
                        EntityL = Label(
                            ScreenTK, text="Write the entity's name:").place(x=10, y=10)
                        EntityE = Entry(
                            ScreenTK, textvariable=Entity, width=37).place(x=10, y=30)
                        Button(ScreenTK, text="Add Entity", command=lambda:
                               self.AddState(Entity, EntitiesT), cursor="hand1").place(x=250, y=26)
                        EntitiesL = Label(
                            ScreenTK, text="Entities: ").place(x=10, y=60)
                        Entities = Label(
                            ScreenTK, textvariable=EntitiesT).place(x=70, y=60)
                        Conditions = Label(
                            ScreenTK, text="Conditions:").place(x=10, y=80)
                        RulesT = Label(
                            ScreenTK, text=" to the condition you are going to use*").place(x=10, y=112)
                        Rules = Label(
                            ScreenTK, text="*Write the entity's name in the space corresponding").place(x=10, y=100)
                        C1 = Label(ScreenTK, text="1. Can't Drive:").place(
                            x=10, y=130)
                        NoDrive = StringVar()
                        C1T = Entry(ScreenTK, textvariable=NoDrive,
                                    width=20).place(x=110, y=130)
                        Button(ScreenTK, text="Add Constraint",
                               command=lambda: self.CantDrive(NoDrive), cursor="hand1").place(x=250, y=125)
                        C2 = Label(ScreenTK, text="2. Can't stay together:  __________________    whitout:").place(
                            x=10, y=160)
                        NoTog = StringVar()
                        Guard = StringVar()
                        C2T = Entry(ScreenTK, textvariable=NoTog,
                                    width=20).place(x=160, y=160)
                        C2T1 = Entry(ScreenTK, textvariable=Guard,
                                     width=20).place(x=350, y=160)
                        Button(ScreenTK, text="Add Constraint",
                               command=lambda: self.NoAloneTog(NoTog, Guard), cursor="hand1").place(x=490, y=155)
                        C3 = Label(ScreenTK, text="3. Can't stay more: __________________    that:").place(
                            x=10, y=190)
                        NoMore = StringVar()
                        That = StringVar()
                        C3T = Entry(ScreenTK, textvariable=NoMore,
                                    width=20).place(x=130, y=190)
                        C3T1 = Entry(ScreenTK, textvariable=That,
                                     width=20).place(x=300, y=190)
                        Button(ScreenTK, text="Add Constraint",
                               command=lambda: self.NoMore(NoMore, That), cursor="hand1").place(x=440, y=185)
                        C4 = Label(ScreenTK, text="4. Can't stay alone:").place(
                            x=10, y=220)
                        NoAlone = StringVar()
                        C4T = Entry(ScreenTK, textvariable=NoAlone,
                                    width=20).place(x=140, y=220)
                        Button(ScreenTK, text="Add Constraint",
                               command=lambda: self.NotAlone(NoAlone), cursor="hand1").place(x=280, y=215)
                        C5 = Label(ScreenTK, text="5. Drive alone:").place(
                            x=10, y=250)
                        DAlone = StringVar()
                        C5T = Entry(ScreenTK, textvariable=DAlone,
                                    width=20).place(x=110, y=250)
                        Button(ScreenTK, text="Add Constraint",
                               command=lambda: self.DriveAlone(DAlone), cursor="hand1").place(x=250, y=245)
                        C6 = Label(ScreenTK, text="6. No Drive: ____________          with:  ____________").place(
                            x=10, y=280)
                        ND = StringVar()
                        W = StringVar()
                        C6T = Entry(ScreenTK, textvariable=ND,
                                    width=20).place(x=90, y=280)
                        C6T1 = Entry(ScreenTK, textvariable=W,
                                     width=20).place(x=260, y=280)
                        Button(ScreenTK, text="Add Constraint", command=lambda: self.NoDriveW(
                            ND, W), cursor="hand1").place(x=400, y=275)
                        C7 = Label(ScreenTK, text="7. Max raft weigth: ").place(
                            x=10, y=310)
                        MW = IntVar()
                        C7T = Entry(ScreenTK, textvariable=MW,
                                    width=20).place(x=130, y=310)
                        Button(ScreenTK, text="Add Constraint",
                               command=lambda: self.MaxWeight(ScreenTK, MW)).place(x=270, y=305)
                        Button(ScreenTK, text="OK",
                               command=lambda: self.StartG(ScreenTK), cursor="hand1").place(x=280, y=335)
                        ScreenTK.mainloop()
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if not self.start:
                if (pygame.mouse.get_pos()[0] >= PlayB.x and pygame.mouse.get_pos()[0] <= PlayB.x + 150
                        and pygame.mouse.get_pos()[1] >= PlayB.y and pygame.mouse.get_pos()[1] <= PlayB.y + 150):
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                Screen.blit(Background, (0, 0))
                PlayB.update(Screen, cursor, play)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                Screen.fill((255, 255, 255))
                self.DrawG(Screen, font)

            cursor.update()
            pygame.display.update()

    def StartG(self, st):
        self.start = True
        self.Graph.Start()
        st.destroy()

    def AddState(self, entity, entities):
        temp = ''
        entN = ''
        dig = True
        if entity.get() != '':
            self.State[0].append(entity.get())
            for i in range(len(entity.get())):
                if entity.get()[i].isdigit() and dig:
                    temp = temp + entity.get()[i]
                else:
                    dig = False
                    break
            if temp != '':
                self.Graph.StateInitN[0].append(int(temp))
            else:
                self.Graph.StateInitN[0].append(1)

            self.Graph.StateInit[0].append(entity.get())
            entities.set(f"{self.State[0]}")
            entity.set('')

    def DrawG(self, Screen, font):
        color = (0, 0, 0)
        drawL = True
        for Edge in self.Graph.Edges:
            drawL = True
            if (Edge.Origin.x and Edge.Destiny.x and Edge.Origin.y and Edge.Destiny.y) != 0:
                for i in range(len(self.Graph.Min) - 1):
                    if ((self.Graph.Min[i] == Edge.Origin and self.Graph.Min[i + 1] == Edge.Destiny)
                            or (self.Graph.Min[i + 1] == Edge.Origin and self.Graph.Min[i] == Edge.Destiny)):
                        drawL = False
                        pygame.draw.line(Screen, (0, 255, 0), (Edge.Origin.x,
                                                               Edge.Origin.y), (Edge.Destiny.x, Edge.Destiny.y), 3)
                        break
                if drawL:
                    pygame.draw.line(Screen, (0, 0, 0), (Edge.Origin.x,
                                                         Edge.Origin.y), (Edge.Destiny.x, Edge.Destiny.y), 3)

        for Node in self.Graph.Nodes:
            width1 = 0
            width2 = 0
            size = 0
            State1 = None
            State2 = None
            Pos = None
            if (Node.x and Node.y) != 0:
                if Node.Accept:
                    color = (255, 0, 0)
                elif Node == self.Graph.Root:
                    color = (0, 0, 255)
                else:
                    color = (0, 0, 0)
                State1 = font.render(f"{Node.State[0]}", True, color)
                State2 = font.render(f"{Node.State[1]}", True, color)
                Pos = font.render(f"{Node.Pos}", True, color)
                width1 = State1.get_width()
                width2 = State2.get_width()
                if width1 >= width2:
                    size = width1 + Pos.get_width()
                else:
                    size = width2 + Pos.get_width()

                pygame.draw.rect(Screen, (255, 255, 255),
                                 (Node.x - 30, Node.y - 15, size, 20))
                Screen.blit((State1), (Node.x - 20, Node.y - 15))
                Screen.blit((State2), (Node.x - 20, Node.y - 5))
                Screen.blit((Pos), (Node.x - 30, Node.y - 10))

    def CantDrive(self, CantDrive):
        cant = ''
        for i in range(len(CantDrive.get())):
            if CantDrive.get()[i] != ',' and CantDrive.get()[i] != '':
                cant = cant + CantDrive.get()[i]
            if CantDrive.get()[i] == ',' or i == len(CantDrive.get()) - 1:
                self.Graph.NoDrive.append(cant)
                cant = ''
        CantDrive.set('')

    def NoAloneTog(self, NoAlone, Guard):
        NoA = []
        entity = ''
        gu = ''
        guards = []
        for ent in NoAlone.get():
            if ent != ',' and ent != '':
                entity = entity + ent
            if ent == ',' or ent == NoAlone.get()[len(NoAlone.get()) - 1]:
                NoA.append(entity)
                entity = ''

        self.Graph.NoAloneTog.append(NoA)

        for guard in Guard.get():
            if guard != ',' and guard != '':
                gu = gu + guard
            if guard == ',' or guard == Guard.get()[len(Guard.get()) - 1]:
                if gu != '':
                    guards.append(gu)
                gu = ''

        self.Graph.Guard.append(guards)
        NoAlone.set('')
        Guard.set('')

    def NoMore(self, NoM, That):
        NoMore = [NoM.get(), That.get()]
        self.Graph.NoMore.append(NoMore)
        NoM.set('')
        That.set('')

    def NotAlone(self, NoAlone):
        entity = ''
        for ent in NoAlone.get():
            if ent != ',' and ent != '':
                entity = entity + ent
            if ent == ',' or ent == NoAlone.get()[len(NoAlone.get()) - 1]:
                self.Graph.NotAlone.append(entity)
                entity = ''
        NoAlone.set('')

    def DriveAlone(self, Drive):
        entity = ''
        for ent in Drive.get():
            if ent != ',' and ent != '':
                entity = entity + ent
            if ent == ',' or ent == Drive.get()[len(Drive.get()) - 1]:
                self.Graph.DriveAlone.append(entity)
                entity = ''
        Drive.set('')

    def NoDriveW(self, ND, W):
        NDrive = [ND.get(), W.get()]
        self.Graph.NoDriveWith.append(NDrive)
        ND.set('')
        W.set('')

    def MaxWeight(self, root, MW):
        if int(MW.get()) > 0:
            self.Graph.MaxWeight = MW.get()
            Entries = [[], []]
            size = self.screen_size()
            ScreenTK = tkinter.Toplevel(root)
            size1 = [500, 0]
            if len(self.Graph.StateInit[0]) > len(self.Graph.StateInit[1]):
                size1[1] = len(self.Graph.StateInit[0]) * 60
            else:
                size1[1] = len(self.Graph.StateInit[1]) * 60

            ScreenTK.geometry(
                f"{size1[0]}x{size1[1]}+{int(size[0]/2) - 250}+{int(size[1]/2) - int(size1[1]/2)}")
            ScreenTK.title("Entity's weight")
            ScreenTK.resizable(0, 0)
            Ins = Label(ScreenTK, text="Write the weight correspondent to each entity:").place(
                x=10, y=10)
            ant = 10
            for i in range(len(self.Graph.StateInit)):
                for ent in self.Graph.StateInit[i]:
                    self.Graph.EWeight[i].append(0)

            for j in range(len(self.Graph.StateInit[0])):
                if self.Graph.StateInit[0][j] != '':
                    W = IntVar()
                    pos = 30 + ant
                    Ent1L = Label(ScreenTK, text=f"{self.Graph.StateInit[0][j]}'s weight:").place(
                        x=10, y=pos)
                    Ent1E = Entry(ScreenTK, textvariable=W,
                                  width=5)
                    Ent1E.place(x=90, y=pos)
                    Entries[0].append(Ent1E)
                    Button(ScreenTK, text="Insert weigth",
                           command=lambda: self.AddWeight(W, Entries), cursor="hand1").place(x=130, y=(pos - 5))
                    ant = pos

            ant = 10
            for k in range(len(self.Graph.StateInit[1])):
                if self.Graph.StateInit[1][k] != '':
                    W = IntVar()
                    pos = 30 + ant
                    Ent2L = Label(ScreenTK, text=f"{self.Graph.StateInit[1][k]}'s weight:").place(
                        x=260, y=pos)
                    Ent2E = Entry(ScreenTK, textvariable=W,
                                  width=5)
                    Ent2E.place(x=340, y=pos)
                    Entries[1].append(Ent2E)
                    Button(ScreenTK, text="Insert weigth",
                           command=lambda: self.AddWeight(W, 1, k), cursor="hand1").place(x=380, y=(pos-5))
                    ant = pos

            Button(ScreenTK, text="OK", command=lambda: ScreenTK.destroy(),
                   cursor="hand1").place(x=230, y=size1[1] - 30)

    def AddWeight(self, W, Entries):
        P1 = 0
        P2 = 0
        ready = False
        for i in range(len(Entries)):
            for j in range(len(Entries[i])):
                if int(Entries[i][j].get()) != 0:
                    W.set(Entries[i][j].get())
                    P1 = i
                    P2 = j
                    ready = True
                    break
            if ready:
                break

        self.Graph.EWeight[P1][P2] = W.get()
        W.set(0)
        print(self.Graph.EWeight)
