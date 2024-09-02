from Dijkstra import Graph

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4,True)  # D - A, weight 4
g.add_edge(3, 4, 2,True)  # D - E, weight 2
g.add_edge(0, 2, 3,True)  # A - C, weight 3
g.add_edge(0, 4, 4,False)  # A - E, weight 4
g.add_edge(4, 2, 4,True)  # E - C, weight 4
g.add_edge(4, 6, 5,True)  # E - G, weight 5
g.add_edge(2, 5, 5,True)  # C - F, weight 5
g.add_edge(2, 1, 2,True)  # C - B, weight 2
g.add_edge(1, 5, 2,True)  # B - F, weight 2
g.add_edge(6, 5, 5,True)  # G - F, weight 5

# Algoritmo de Dijkstra desde A hacia los demas vertices
print("\nAlgoritmo de Dijkstra, tomando como vertice inicial A:")
distances = g.dijkstra('A')
for i, d in enumerate(distances):
    print(f"Distancia de A hacia {g.vertex_data[i]}: {d}")