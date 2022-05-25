import matplotlib.pyplot as plt
import networkx as nx

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

    def kruskalAlgo(self):
        pass
        # Buraya Prim Algoritmasnı yerleştirsen yeterli
        self.printSolution()

    def printSolution(self):
        pass

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

a=0
for s,d,w in G.MST:
    a += int(w)
    print(f'{s}-{d}: {w}')
print(f'Minimum yayılan ağacın toplam ağırlığı: {a}')

D = nx.Graph()

for i in G.nodes:
    D.add_node(i)

for s,d,w in G.MST:
    D.add_edge(s,d, weight = w)

elarge = [(u, v) for (u, v, d) in D.edges(data=True)]
esmall = [(u, v) for (u, v, d) in D.edges(data=True)]

pos = nx.spring_layout(D, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(D, pos, node_size=700)

# edges
nx.draw_networkx_edges(D, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    D, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(D, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(D, "weight")
nx.draw_networkx_edge_labels(D, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
