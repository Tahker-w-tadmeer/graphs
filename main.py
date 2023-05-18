from graph_v2 import Graph
from prim import Prim
from dijkstra import Dijkstra
g = Graph(9, directed=False)

g.insert_edge((0, 1), 4) # a, b
g.insert_edge((1, 2), 8) # b, c
g.insert_edge((2, 3), 7) # c, d
g.insert_edge((3, 4), 9) # d, e
g.insert_edge((4, 5), 10) # e, f
g.insert_edge((3, 5), 14) # d, f

g.insert_edge((5, 6), 2) # f, g
g.insert_edge((6, 7), 1) # g, h
g.insert_edge((7, 8), 7) # h, i
g.insert_edge((8, 2), 2) # i, c
g.insert_edge((2, 5), 4) # c, f
g.insert_edge((0, 7), 8) # a, h
g.insert_edge((1, 7), 11) # b, h
g.insert_edge((6, 8), 6) # g, i

g.display_graph()

graph = Prim.create_spanning_tree(g, 0)
graph2, sum = Prim.calc_mst(g, 0)
print("Minimum Spanning Tree: \n")
graph.display_graph()
print("\nMinimum Spanning Tree: \n")
print(graph2)
print(sum)

p,s = Dijkstra.dijkstra_algorithm(g,0)
print(p)
print(s)
