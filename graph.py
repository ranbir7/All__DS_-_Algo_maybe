class graph:
    def __init__(self):
        self.graph = dict()

    def addVertex(self, node):
        self.graph[node] = list()

    def addEdge(self, node, value):
        if value in self.graph[node]:
            return
        self.graph[node].append(value)
        if value in self.graph.keys():
            self.graph[value].append(node)

    def printGraph(self):
        for i in self.graph.keys():
            print(f'{i}-->{self.graph[i]}')
    
    #Previously created Function printGrph
    """
       def showGraph(self):
          for i in self.GraphC:
            print('{} --> {}'.format(i, list(set(self.GraphC[i]))))
    """
c= graph()          
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
c.printGraph()
