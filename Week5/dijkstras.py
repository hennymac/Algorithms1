import heapq

class Node(object):

    def __init__(self,id,neighbors):
        self.id = id
        self.neighbors = {k:v for k,v in neighbors}
        self.dist = float('inf')
        self.parent = None
        self.found = False

    def __cmp__(self,other):
        return cmp(self.dist,other.dist)

    def getDist(self):
        return self.dist

    def getID(self):
        return self.id

    def getNeighbors(self):
        return self.neighbors.keys()

    def setDistance(self,value):
        self.dist = value

    def makeFound(self):
        self.found = True

    def isFound(self):
        return self.found

    def updateDist(self,neighbor):
        if neighbor.getID() in self.getNeighbors():
            newDist = neighbor.getDist() + self.neighbors[neighbor.getID()]
            if newDist < self.dist:
                self.dist = newDist
                self.parent = neighbor.getID()

    def __str__(self):
        return 'Node: ' + str(self.id)

def dijkstra(Graph,start):
    Graph[start].setDistance(0)
    heap = Graph.values()
    heapq.heapify(heap)
    while heap:
        x = heapq.heappop(heap)
        x.makeFound()
        for neighbor in x.getNeighbors():
            if not Graph[neighbor].isFound():
                Graph[neighbor].updateDist(x)
        heapq.heapify(heap)

    return Graph






def loadData(filename):

    with open(filename,"r") as f:
        graph = [line.split() for line in f]
    G = {}
    for node in graph:
        node_id = int(node[0])
        neighbors = [map(int,i.split(',')) for i in node[1:]]
        G[node_id] = Node(node_id,neighbors)

    return G

def main(filename,start_node):
    #filename = 'SCC.txt'
    #filename = 'test2.txt'

    G = loadData(filename)

    return dijkstra(G,start_node)
