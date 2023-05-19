from graph import Graph
import sys


class Dijkstra:

    @staticmethod
    def calculate(graph, start_node) -> Graph:
        unvisited_nodes = list(range(0, graph.no_vertices))
        answer = Graph(graph.no_vertices, directed=True)
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
        shortest_path = {}
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}

        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0
        shortest_path[start_node] = 0

        # The algorithm executes until we visit all nodes
        while unvisited_nodes:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + neighbor.weight
                if tentative_value < shortest_path[neighbor.vertex]:
                    shortest_path[neighbor.vertex] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor.vertex] = (current_min_node, neighbor.vertex, tentative_value)

            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)

        for i in previous_nodes:
            vertex1, vertex2, weight = previous_nodes[i]
            answer.insert_edge((vertex1, vertex2), weight)

        return answer
