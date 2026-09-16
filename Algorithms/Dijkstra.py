import heapq

def djikstra(graph, start): 
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
    
def dijkstra_array(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = None
        min_distance = float('inf')
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break

        visited.add(min_node)

        for neighbor, weight in graph[min_node].items():
            if neighbor not in visited:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances