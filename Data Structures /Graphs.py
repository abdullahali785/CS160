import heapq
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, e, v):
        self.graph[e].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)
    
    def dfs_path(self, start, target, path=None, visited=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        visited.add(start)
        path.append(start)

        if start == target:
            return path 
        
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                result = self.dfs_path(neighbour, target, path, visited)
                if result:
                    return result 
                
        return None 

    def bfs(self, start): 
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)

                for neighbour in self.graph[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour) 

    def djikstra(self, graph, start): 
        distances = {node : float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbour, weight in graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(pq, (distance, neighbour))

        return distances 
    
    def dijkstra_array(self, graph, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.graph):
            min_node = None
            min_distance = float('inf')
            for node in self.graph:
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    min_node = node

            if min_node is None:
                break

            visited.add(min_node)

            for neighbor, weight in self.graph[min_node].items():
                if neighbor not in visited:
                    new_distance = distances[min_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        return distances

        

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

# print(g.dfs('A'))

# print(g.bfs('A'))

print(g.dijkstra_array(g, 'A'))

# print(g.dfs_path('A', 'E'))

# G = {
#     'A': {'B': 5, 'C': 10},
#     'B': {'C': 3, 'D': 9},
#     'C': {'D': 1},
#     'D': {}
# }

# print(g.dijkstra(G, 'A'))
