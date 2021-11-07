class Graph:
    def __init__(self):
        self.nodes = 0
        self.GraphC = {}

    def addVertex(self, key_value):
        if key_value in self.GraphC.keys():
            print('Duplicate Vertexes Are Not Allowed')

            return
        else:
            self.GraphC[key_value] = []
            self.nodes += 1

    def addEdge(self, key_value, value_member):
        if key_value in self.GraphC.keys():
            self.GraphC[key_value] += value_member
            self.GraphC[value_member] += key_value
            return
        else:
            print('Duplicate Edges Are Not Allowed')
            return

    def showGraph(self):
        for i in self.GraphC:
            print('{} --> {}'.format(i, list(set(self.GraphC[i]))))


c = Graph()
c.addVertex('0')
c.addVertex('1')
c.addVertex('2')
c.addVertex('3')
c.addVertex('4')
c.addVertex('5')
c.addVertex('6')
c.addEdge('3', '1')
c.addEdge('3', '4')
c.addEdge('0', '1')
c.addEdge('0', '2')
c.addEdge('2', '4')
c.addEdge('2', '1')
c.addEdge('4', '5')
c.addEdge('5', '6')
c.addEdge('1','2')
c.addEdge('1','3')
c.showGraph()
print('The Number Of Vertexes is:',c.nodes)