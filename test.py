from graph_v2 import Graph
from prim import Prim

g = Graph(9, directed=False)

g.insert_edge((0, 1), 4)
g.insert_edge((1, 2), 8)
g.insert_edge((2, 3), 7)
g.insert_edge((3, 4), 9)
g.insert_edge((4, 5), 10)
g.insert_edge((3, 5), 14)
g.insert_edge((5, 6), 2)
g.insert_edge((6, 7), 1)
g.insert_edge((7, 8), 7)
g.insert_edge((8, 2), 2)
g.insert_edge((2, 5), 2)
g.insert_edge((0, 7), 8)
g.insert_edge((2, 5), 10)
g.insert_edge((6, 8), 6)

g.display_graph()

graph = Prim.create_spanning_tree(g, 0)
print("Minimum Spanning Tree: \n")
graph.display_graph()
