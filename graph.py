class Node:
    def __init__(self, name, weight):
        self.next = None
        self.name = name
        self.weight = weight


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # self.edges = [[0] * num_vertices] * num_vertices
        self.heads = [None] * num_vertices

    def add_edge(self, src: int, dest: int, weight: int):
        # self.edges[src][dest] = weight
        # self.edges[dest][src] = weight
        new_node = Node(dest, weight)
        new_node.next = self.heads[src]
        self.heads[src] = new_node

        new_node = Node(src, weight)
        new_node.next = self.heads[dest]
        self.heads[dest] = new_node

    def traverse(self):
        for edge in self.heads:
            temp = self
            while temp:
                print(temp.vertex, end='-->')
                temp = temp.next

    def print_graph(self):
        for edge in self.heads:
            #if edge is None:
               # continue

            next_edge = edge
            while next_edge is not None:
                print(str(next_edge.name) + " -" + str(next_edge.weight) + "-> ")
            print("None\n")

