import heapq

def dijkstra(graph, start, end):
    # Mappa dei predecessori
    predecessors = {}
    # Mappa dei pesi
    weights = {}
    # Inizializzazione delle mappe
    for node in graph:
        weights[node] = float('inf')
        predecessors[node] = None
    weights[start] = 0
    # Inserimento dei nodi nella coda di priorità
    queue = []
    for node in graph:
        heapq.heappush(queue, (weights[node], node))
    # Ciclo principale
    while queue:
        current_weight, current_node = heapq.heappop(queue)
        if current_node == end:
            # Costruzione del percorso ottimo
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = predecessors[current_node]
            return path[::-1]
        for neighbor, edge_attr in graph[current_node].items():
            weight = edge_attr['weight']
            new_weight = current_weight + weight
            if new_weight < weights[neighbor]:
                weights[neighbor] = new_weight
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (new_weight, neighbor))
    return []
