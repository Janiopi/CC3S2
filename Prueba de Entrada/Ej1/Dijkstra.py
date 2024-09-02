class Graph:
   
    
    def __init__(self, size):   #Creacion del grafo a partir del numero de vertices
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

   
    def add_edge(self, u, v, weight, directed):
        if 0 <= u < self.size and 0 <= v < self.size: #Verificando que los vertices de la arista se encuentren en el rango admitido
            
            if(directed):
                self.adj_matrix[u][v] = weight # En caso que sea una arista direccionada, de u a v
            else:
                self.adj_matrix[u][v] = weight  #En caso que no sea una arista direccionada 
                self.adj_matrix[v][u] = weight  
                       

    def add_vertex_data(self, vertex, data):  
        if 0 <= vertex < self.size:            #Verificando que el vertice se encuentre en el rango admitido
            self.vertex_data[vertex] = data   #Añadiendo un peso a cada vertice

    def dijkstra(self, start_vertex_data):      
        start_vertex = self.vertex_data.index(start_vertex_data)    # Señalando el vertice de inicio
        distances = [float('inf')] * self.size                      # Asignando a todas las distancias el valor inf
        distances[start_vertex] = 0                                 # Cero, a la distancia hacia el vertice inicial    
        visited = [False] * self.size                               # Marcando todos los vertices como no visitados

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:        # Se recorre todos los vertices no visitados, escogiendo a los de menor distancia
                    min_distance = distances[i]
                    u = i

            if u is None:
                break                                                     # En caso no se haya encontrado un vertice de menor peso

            visited[u] = True                                             #En caso que si, se marca como visitado

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:       
                    alt = distances[u] + self.adj_matrix[u][v]          # El vertice no visitado es añadido al camino
                    if alt < distances[v]:                              # Verifica que el camino tenga el menor peso posible
                        distances[v] = alt

        return distances


