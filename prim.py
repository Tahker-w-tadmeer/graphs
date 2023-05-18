import heapq
from graph import Graph


class Prim:
    @staticmethod
    def calculate(graph: Graph, src: int) -> (Graph, int):
        num_vertices = graph.no_vertices
        answer = Graph(graph.no_vertices, directed=False)
        visited = [False] * num_vertices  # to track visited vertices
        start_vertex = src  # start with the first vertex
        num_visited = 1  # number of visited vertices
        sum_of_weight = 0
        # Create a priority queue to store (weight, parent_vertex, vertex) tuples
        priority_queue = []
        heapq.heappush(priority_queue, (0, None, start_vertex))  # Start with the first vertex

        while priority_queue:
            weight, parent_vertex, vertex = heapq.heappop(priority_queue)
            if visited[vertex]:
                continue

            visited[vertex] = True
            num_visited += 1

            if parent_vertex is not None:
                answer.insert_edge((parent_vertex, vertex), weight)
                sum_of_weight += weight

            # Visit the adjacent vertices and add them to the priority queue
            current_node = graph.vertices_list[vertex].head
            while current_node:
                if not visited[current_node.vertex]:
                    heapq.heappush(priority_queue, (current_node.weight, vertex, current_node.vertex))
                current_node = current_node.next

        return answer, sum_of_weight
