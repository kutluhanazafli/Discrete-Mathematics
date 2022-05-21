import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge("A", "B", weight=3)
G.add_edge("B", "C", weight=1)
G.add_edge("C", "D", weight=1)
G.add_edge("A", "E", weight=2)
G.add_edge("A", "F", weight=4)
G.add_edge("B", "F", weight=2)
G.add_edge("C", "F", weight=4)
G.add_edge("C", "G", weight=1)
G.add_edge("D", "G", weight=1)
G.add_edge("D", "H", weight=5)
G.add_edge("E", "F", weight=5)
G.add_edge("F", "G", weight=3)
G.add_edge("G", "H", weight=5)
G.add_edge("E", "I", weight=1)
G.add_edge("F", "I", weight=6)
G.add_edge("F", "J", weight=3)
G.add_edge("I", "J", weight=2)
G.add_edge("G", "J", weight=3)
G.add_edge("G", "K", weight=3)
G.add_edge("J", "K", weight=3)
G.add_edge("G", "L", weight=2)
G.add_edge("G", "L", weight=2)
G.add_edge("K", "L", weight=4)
G.add_edge("H", "L", weight=2)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
