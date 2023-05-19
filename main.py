from graph import Graph
from prim import Prim
from dijkstra import Dijkstra


print("Prim:\n")
graph = Graph(9, directed=False)

graph.insert_edge((0, 1), 4) # a, b
graph.insert_edge((1, 2), 8) # b, c
graph.insert_edge((2, 3), 7) # c, d
graph.insert_edge((3, 4), 9) # d, e
graph.insert_edge((4, 5), 10) # e, f
graph.insert_edge((3, 5), 14) # d, f
graph.insert_edge((5, 6), 2) # f, g
graph.insert_edge((6, 7), 1) # g, h
graph.insert_edge((7, 8), 7) # h, i
graph.insert_edge((8, 2), 2) # i, c
graph.insert_edge((2, 5), 4) # c, f
graph.insert_edge((0, 7), 8) # a, h
graph.insert_edge((1, 7), 11) # b, h
graph.insert_edge((6, 8), 6) # g, i

graph.display_graph()

mst, sum_of_weights = Prim.calculate(graph, 0)
print("\nMinimum Spanning Tree:\n")
mst.display_graph()
print("Shortest distance: " + str(sum_of_weights))

print("\n--------------------\n")
print("Dijkstra:\n")

graph2 = Graph(5, directed=True)
graph2.insert_edge((0, 1), 10) # s, t
graph2.insert_edge((1, 2), 1) # t, x
graph2.insert_edge((2, 3), 4) # x, z
graph2.insert_edge((3, 2), 6) # z, x
graph2.insert_edge((3, 0), 7) # z, s
graph2.insert_edge((0, 4), 5) # s, y
graph2.insert_edge((4, 3), 2) # y, z
graph2.insert_edge((1, 4), 2) # t, y
graph2.insert_edge((4, 1), 3) # y, t
graph2.insert_edge((4, 2), 9) # y, x

graph2.display_graph()

print("\nShortest Path: \n")
sp = Dijkstra.calculate(graph2, 0)
sp.display_graph()
