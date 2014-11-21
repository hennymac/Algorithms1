

class Track(object):
    """Keeps track of explored, time, source, leader, et cetera"""
    def __init__(self,explored):
        self.explored = explored
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_times = {}

    def addNode(self,node):
        """adds node to SCC group"""
        self.leader[self.current_source] = self.leader.get(self.current_source,[]) + [node]

def scc(graph,reverse_graph,nodes):

    explored = [False for i in range(len(nodes))]
    track = Track(explored)
    dfs_loop(reverse_graph,nodes,track)
    sorted_nodes = sorted(track.finish_times, key=track.finish_times.get,reverse=True)
    explored = [False for i in range(len(nodes))]
    track = Track(explored)
    dfs_loop(graph,sorted_nodes,track)
    return track

def dfs(graph,start,track):
    track.explored[start] = True
    track.addNode(start)
    for edge in graph[start]:
        if not track.explored[edge]:
            dfs(graph,edge,track)
    track.current_time += 1
    track.finish_times[start] = track.current_time


def dfs_loop(graph,nodes,track):
    for node in nodes:
        if not track.explored[node]:
            track.current_source = node
            dfs(graph,node,track)

def loaddata(filename):

    with open(filename,"r") as f:
        edges = [map(int,line.split()) for line in f]
        #G = {int(line.split()[0]): G.get(int(line.split()[0],[]) + map(int,line.split()[1:]) for line in f}
        # nodes = [[int(s) for s in line.split()] for line in f]
        # G = {node[0]: node[1:] for node in nodes}

    nodes = list(set([v-1 for edge in edges for v in edge]))
    G = [[] for i in range(len(nodes))]
    Grev = [[] for i in range(len(nodes))]
    for edge in edges:
        G[edge[0]-1] += [edge[1]-1]
        Grev[edge[1]-1] += [edge[0]-1]

    return G,Grev,nodes

def main(filename):
    #filename = 'SCC.txt'
    #filename = 'test2.txt'

    G,Grev,nodes = loaddata(filename)

    return scc(G,Grev,nodes)

