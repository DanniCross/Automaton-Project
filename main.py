from Resources.CrossRiver import CrossRiver
from Views.GUI import GUI
from Resources.ReadJSON import Read


def main():
    cross = CrossRiver()
    read = Read(cross)
    GUI(read)


main()
