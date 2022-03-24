from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        self.totalNodes=nodes
        self.graph=defaultdict(list)


    def addEdge(self, s, d):
        self.graph[s].append(d)


    def getVertexCover(self):
        visited=[False]*(self.totalNodes)

        for u in range(self.totalNodes):
            if not visited[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[v]=True
                        visited[u]=True
                        break

        for j in range(self.totalNodes):
            if visited[j]:
                print(j, end=' ')

        print()

g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,5)
g.addEdge(1,2)
g.addEdge(2,4)
g.addEdge(2,3)
g.addEdge(5,4)
g.addEdge(1,5)

# answer found is at most 2 times the weight of the Optimal Minimum Vertex Cover.
g.getVertexCover()


