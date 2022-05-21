class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))


class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


def kruskalAlgo(self):
    i, e = 0, 0
    ds = dst.DisjointSet(self.nodes)
    self.graph = sorted(self.graph, key=lambda item: item[2])
    while e < self.V - 1:
        s, d, w = self.graph[i]
        i += 1
        x = ds.find(s)
        y = ds.find(d)
        if x != y:
            e += 1
            self.MST.append([s, d, w])
            ds.union(x, y)
    self.printSolution(s, d, w)


G = Graph(12)
G.addNode("A")
G.addNode("B")
G.addNode("C")
G.addNode("D")
G.addNode("E")
G.addNode("F")
G.addNode("G")
G.addNode("H")
G.addNode("I")
G.addNode("J")
G.addNode("K")
G.addNode("L")
G.addEdge("A", "B", 3)
G.addEdge("B", "C", 1)
G.addEdge("C", "D", 1)
G.addEdge("A", "E", 2)
G.addEdge("A", "F", 4)
G.addEdge("B", "F", 2)
G.addEdge("C", "F", 4)
G.addEdge("C", "G", 1)
G.addEdge("D", "G", 1)
G.addEdge("D", "H", 5)
G.addEdge("E", "F", 5)
G.addEdge("F", "G", 3)
G.addEdge("G", "H", 5)
G.addEdge("E", "I", 1)
G.addEdge("F", "I", 6)
G.addEdge("F", "J", 3)
G.addEdge("I", "J", 2)
G.addEdge("G", "J", 3)
G.addEdge("G", "K", 3)
G.addEdge("J", "K", 3)
G.addEdge("G", "L", 2)
G.addEdge("G", "L", 2)
G.addEdge("K", "L", 4)
G.addEdge("H", "L", 2)
G.kruskalAlgo()
