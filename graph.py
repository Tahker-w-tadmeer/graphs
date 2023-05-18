class Node:
    def __init__(self, vertex=None, weight=0):
        self.vertex = vertex
        self.next = None
        self.weight = weight


# implementation of linked list for the graph
class LinkedList:
    def __init__(self):
        self.head = None

    # add a vertex in the linked list
    def insert(self, vertex, weight):
        node = Node(vertex, weight)  # create a node
        if self.head is None:  # if list is empty insert a vertex(node) at the start
            self.head = node
        else:
            temp = self.head
            # iterate through the list till last node is found
            while temp.next:
                temp = temp.next
            temp.next = node  # adding a new node

    # traverse through a linked list
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.vertex, end="(" + str(temp.weight) + ")--> ")
            temp = temp.next


# representation of graph using linked lists
class Graph:
    def __init__(self, no_vertices, directed=True):
        self.no_vertices = no_vertices
        self.vertices_list = [LinkedList() for i in range(0, no_vertices)]  # create a list to represent the graph
        self.directed = directed

        # insert an edge in the graph

    def insert_edge(self, edge, weight):
        vertex1, vertex2 = edge
        if (0 <= vertex1 < self.no_vertices) and (0 <= vertex2 < self.no_vertices):
            # add an edge from vertex1 to vertex2
            self.vertices_list[vertex1].insert(vertex2, weight)
            if not self.directed:  # if the graph is undirected, add an edge from vertex2 to vertex1 as well
                self.vertices_list[vertex2].insert(vertex1, weight)
        else:
            raise ValueError("Invalid vertices")

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.vertices_list:
            if self.vertices_list[node].head:
                connections.append(out_node)
        return connections

    # display the graph
    def display_graph(self):
        for i in range(0, self.no_vertices):
            print(i, end="\t")
            self.vertices_list[i].traverse()
            print("None")

        print("\n")
