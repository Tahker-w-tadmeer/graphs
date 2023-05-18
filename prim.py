import heapq
from collections import defaultdict
from graph_v2 import Graph
import heapq as hq

INF = float('inf')


class Prim:
    @staticmethod
    def calculate(graph: Graph, src: int) -> Graph:
        pr_q = []
        answer = Graph(graph.no_vertices)
        node = graph.vertices_list[src].head
        hq.heappush(pr_q, (node, 0))
        for vertice in graph.vertices_list:
            hq.heappush(pr_q, (vertice.head, INF))

        while len(pr_q) > 0:
            u = hq.heappop(pr_q)
            next_node = u.next
            minimum = (0, u)
            while next_node is not None:
                next_node = next_node.next

            answer.insert_edge((u.vertex, minimum[1].vertex), minimum[0])

        return answer

    @staticmethod
    def create_spanning_tree(graph, starting_vertex) -> Graph:
        answer = Graph(graph.no_vertices)

        visited = {starting_vertex}
        node = graph.vertices_list[starting_vertex].head
        edges = []
        while node.next is not None:
            edges.append((node.weight, starting_vertex, node.next.vertex))
            node = node.next
        heapq.heapify(edges)

        while edges:
            cost, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                answer.vertices_list[frm].insert(to, cost)
                node = graph.vertices_list[to].head
                edges = []
                while node is not None:
                    to_next = node
                    if to_next.vertex not in visited:
                        heapq.heappush(edges, (cost, to, to_next.vertex))
                    node = node.next

        return answer


    @staticmethod
    def calc_mst(graph: Graph, src: int):
        num_vertices = graph.no_vertices
        mst = []  # to store the minimum spanning tree
        visited = [False] * num_vertices  # to track visited vertices
        start_vertex = 0  # start with the first vertex
        num_visited = 1  # number of visited vertices
        sum = 0
        # Create a priority queue to store (weight, parent_vertex, vertex) tuples
        priority_queue = []
        heapq.heappush(priority_queue, (0, None, start_vertex))  # Start with the first vertex

        while priority_queue and num_visited < num_vertices:
            weight, parent_vertex, vertex = heapq.heappop(priority_queue)
            if not visited[vertex]:
                visited[vertex] = True
                num_visited += 1

                if parent_vertex is not None:
                    mst.append(((parent_vertex, vertex), weight))
                    sum += weight

                # Visit the adjacent vertices and add them to the priority queue
                current_node = graph.vertices_list[vertex].head
                while current_node:
                    if not visited[current_node.vertex]:
                        heapq.heappush(priority_queue, (current_node.weight, vertex, current_node.vertex))
                    current_node = current_node.next

        return mst,sum

        

