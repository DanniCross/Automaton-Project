class Read:

    def __init__(self, Graph):
        self.file = 'Assets/Automaton_Definition.txt'
        self.Graph = Graph

    def Read(self):
        with open(self.file, 'r') as txt:
            text = txt.readlines()


def main():
    read = Read()
    read.Read()


main()
