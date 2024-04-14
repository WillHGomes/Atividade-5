import heapq

def dijkstra(graph, start, end):
    # Dicionário para armazenar as distâncias mínimas de start para cada vértice
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # A distância de start para ele mesmo é 0
    # Inicializa uma fila de prioridade
    pq = [(0, start)]  # Uma tupla (distância, vértice)
    # Dicionário para armazenar o predecessor de cada vértice no caminho mínimo
    predecessors = {}
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Se chegarmos ao destino, interrompa
        if current_vertex == end:
            break
        
        # Se a distância atual é maior do que a menor distância armazenada, ignore
        if current_distance > distances[current_vertex]:
            continue
        
        # Verifica cada vizinho do vértice atual
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight  # Distância até o vizinho
            
            # Se a distância até o vizinho for menor do que a distância armazenada, atualize-a
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))  # Adiciona o vizinho à fila de prioridade
    
    # Reconstrói o caminho mínimo a partir dos predecessores
    path = []
    while end:
        path.append(end)
        end = predecessors.get(end)
    return path[::-1], distances[path[-1]]

# Exemplo de uso
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 3},
    'D': {'B': 4, 'C': 3}
}
start_vertex = 'A'
end_vertex = 'D'

shortest_path, shortest_distance = dijkstra(graph, start_vertex, end_vertex)
print("Caminho mais curto de", start_vertex, "para", end_vertex, ":", shortest_path)
print("Distância mínima:", shortest_distance)
