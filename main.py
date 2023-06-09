import json
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import dijkstra

# Importazione del grafo dal file graph.json
with open('graph.json', 'r', encoding='utf-8-sig') as file:
    graph_data = json.load(file)

# Creazione del grafo
graph = nx.DiGraph()

# Aggiunta dei nodi al grafo
for node_data in graph_data['nodes']:
    node_id = node_data['id']
    graph.add_node(node_id, id=node_id)

# Aggiunta degli archi al grafo
for arc_data in graph_data['arcs']:
    end1 = arc_data['end1']
    end2 = arc_data['end2']
    weight = arc_data['weight']
    graph.add_edge(end1, end2, weight=weight)

# Scelta dei nodi di partenza e arrivo
start_node = 0
end_node = 4

# Applicazione dell'algoritmo di Dijkstra
shortest_path = dijkstra(graph, start_node, end_node)

# Generazione casuale delle posizioni dei nodi
pos = nx.spring_layout(graph)

# Disegno dei nodi
nx.draw_networkx_nodes(graph, pos, node_color='black', node_size=500)
node_labels = nx.get_node_attributes(graph, 'id')
nx.draw_networkx_labels(graph, pos, labels=node_labels, font_color='white', font_size=8)

# Disegno degli archi del grafo
nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), edge_color='darkgray', width=1, arrows=True)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color='black', font_size=7)

# Definizione degli archi del percorso più breve
path_arcs = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
path_arcs_labels = {(u, v): labels[(u, v)] for u, v in path_arcs}

# Disegno degli archi del percorso più breve
nx.draw_networkx_edges(graph, pos, edgelist=path_arcs, edge_color='blue', width=4, arrows=True, arrowsize=20)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=path_arcs_labels, font_color='red', font_size=10, label_pos=0.5)

# Aggiunta del titolo al grafico
print(shortest_path)
plt.title(f"Percorso più breve: {' -> '.join(map(str, shortest_path))}")

# Visualizzazione del grafico
plt.axis('off')
plt.show()
