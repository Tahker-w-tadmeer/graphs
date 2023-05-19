import heapq
from graph import Graph


class Prim:
    @staticmethod
    def calculate(graph: Graph, start_vertex: int) -> (Graph, int):
        answer = Graph(graph.no_vertices, directed=False)
        visited = [False] * graph.no_vertices
        sum_of_weight = 0
        # (weight, parent_vertex, vertex)
        priority_queue = []
        heapq.heappush(priority_queue, (0, None, start_vertex))

        while priority_queue:
            weight, parent_vertex, vertex = heapq.heappop(priority_queue)
            if visited[vertex]:
                continue

            visited[vertex] = True
            if parent_vertex is not None:
                answer.insert_edge((parent_vertex, vertex), weight)
                sum_of_weight += weight

            # Visit the adjacent vertices and add them to the priority queue
            node = graph.vertices_list[vertex].head
            while node:
                if not visited[node.vertex]:
                    heapq.heappush(priority_queue, (node.weight, vertex, node.vertex))
                node = node.next

        return answer, sum_of_weight
