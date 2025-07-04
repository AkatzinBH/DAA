import random
from node import Node
from edge import Edge
import sys
import collections
import heapdict
import numpy as np

class Graph:
    def __init__(self, id='grafo', dirigido=False):
        self.id = id
        self.dirigido = dirigido
        self.V = dict()
        self.E = dict()
        self.attr = dict()

    def __repr__(self):
        return str("id: " + str(self.id) + '\n'
                   + 'nodos: ' + str(self.V.values()) + '\n'
                   + 'aristas: ' + str(self.E.values()))
    
    def clone(self):
        """
        Crea una copia del grafo actual.
        :return: Un nuevo objeto Grafo que es una copia del grafo actual.
        """
        nuevo_grafo = Graph(id=self.id + "_clone", dirigido=self.dirigido)
        # Clonar nodos
        for nodo in self.V.values():
            nuevo_grafo.add_nodo(Node(nodo.id))
        # Clonar aristas
        for arista in self.E.values():
            nuevo_grafo.add_arista(Edge(nuevo_grafo.V[arista.u.id], nuevo_grafo.V[arista.v.id]))
        return nuevo_grafo
    
    def add_nodo(self, nodo):
        self.V[nodo.id] = nodo

    def get_nodo(self, nodo_id):
        return self.V.get(nodo_id)

    def add_arista(self, arista):
        if self.get_arista(arista.id):
            return False

        self.E[arista.id] = arista
        return True

    def get_arista(self, arista_id):
        if self.dirigido:
            return arista_id in self.E
        else:
            u, v = arista_id
            return (u, v) in self.E or (v, u) in self.E 
           
    def equal_weights(self):
        """
        Asigna un peso igual a todas las aristas del nodo con un valor de 1.
        """
        for arista in self.E.values():
            arista.attrs['weight'] = 1

    def random_weights(self):
        """
        Asigna un peso aleatorio a todas las aristas del nodo con un valor entre 1 y 100.
        """
        for arista in self.E.values():
            arista.attrs['weight'] = random.randint(1, 100)

    def costo(self):
        """
        Calcula el costo del grafo. Suma del peso de las aristas
        costo : float
            suma del peso de las aristas del grafo
        """
        _costo = 0
        for edge in self.E.values():
            _costo += edge.attrs['weight']

        return _costo
    
    def to_graphviz(self, filename):
        edge_connector = "--"
        graph_directive = "graph"
        if self.dirigido:
            edge_connector = "->"
            graph_directive = "digraph"

        with open(filename, 'w') as f:
            f.write(f"{graph_directive} {self.id} " + " {\n")
            for nodo_id, nodo_obj in self.V.items(): # Itera sobre items para obtener id y objeto
                if "Dijkstra" in self.id:
                    # Verifica que 'dist' exista antes de acceder
                    dist_str = str(nodo_obj.attrs.get('dist', 'inf')) # Obtiene 'dist' de attrs del nodo
                    f.write(f"\"{nodo_id} ({dist_str})\";\n")
                else:
                    f.write(f"n_{nodo_id};\n") # Mantiene el formato original para nodos no Dijkstra
            for arista in self.E.values():
                if "Dijkstra" in self.id:
                    # Obtiene las distancias de los nodos de la arista para el label
                    dist_u_str = str(arista.u.attrs.get('dist', 'inf'))
                    dist_v_str = str(arista.v.attrs.get('dist', 'inf'))

                    # Construye las etiquetas de los nodos para las aristas de Dijkstra
                    u_label = f"\"{arista.u.id} ({dist_u_str})\""
                    v_label = f"\"{arista.v.id} ({dist_v_str})\""

                    f.write(f"{u_label} {edge_connector} {v_label};\n")
                else:
                    f.write(f"n_{arista.u.id} {edge_connector} n_{arista.v.id};\n") # Mantiene el formato original para aristas no Dijkstra
            f.write("}")

    def BFS(self, s):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo "breadth first search"
        Parametros
        s : Nodo nodo raíz del árbol que se va a generar
        Returns
        bfs : Grafo árbol generado
        """
        if not s.id in self.V:
            print("Error, el nodo no está en V", file=sys.stderr)
            exit(-1)

        bfs = Graph(id=f"{self.id}_BFS", dirigido=self.dirigido)
        discovered = set()
        bfs.add_nodo(s)
        L0 = [s]
        discovered = set()
        added = [s.id]

        while True:
            L1 = []
            for node in L0:
                aristas = [ids_arista for ids_arista in self.E
                            if node.id in ids_arista]

                for arista in aristas:
                    v = arista[1] if node.id == arista[0] else arista[0]

                    if v in discovered:
                        continue

                    bfs.add_nodo(self.V[v])
                    bfs.add_arista(self.E[arista])
                    discovered.add(v)
                    L1.append(self.V[v])

            L0 = L1
            if not L0:
                break

        return bfs
    
    
    def DFS_R(self, s):
        """
        Realiza una búsqueda en profundidad recursiva (DFS) desde el nodo fuente s.
        (Versión modificada para tratar el grafo como no dirigido)

        :param s: Nodo fuente
        :return: Un nuevo grafo que representa el árbol DFS
        """
        if s.id not in self.V:
            print("Error: El nodo fuente no existe en el grafo.", file=sys.stderr)
            return None

        arbol_dfs = Graph(id=f"{self.id}_DFS_R", dirigido=False)
        visitados = set()

        def _dfs_recursivo(nodo_actual):
            visitados.add(nodo_actual.id)
            arbol_dfs.add_nodo(self.V[nodo_actual.id])

            for arista in self.E.values():
                if arista.u.id == nodo_actual.id and arista.v.id not in visitados:
                    arbol_dfs.add_arista(Edge(self.V[arista.u.id], self.V[arista.v.id]))
                    _dfs_recursivo(self.V[arista.v.id])
                elif arista.v.id == nodo_actual.id and arista.u.id not in visitados:  # Siempre revisa la otra dirección
                    arbol_dfs.add_arista(Edge(self.V[arista.v.id], self.V[arista.u.id]))
                    _dfs_recursivo(self.V[arista.u.id])

        _dfs_recursivo(self.V[s.id])
        return arbol_dfs
    
    def DFS_I(self, s):
            """
            Realiza una búsqueda en profundidad iterativa (DFS) desde el nodo fuente s.
            :param s: Nodo fuente
            :return: Un nuevo grafo que representa el árbol DFS
            """
            if s.id not in self.V:
                print("Error: El nodo fuente no existe en el grafo.", file=sys.stderr)
                return None

            visitados = set()
            pila = [s.id]  # La pila contiene los IDs de los nodos
            arbol_dfs = Graph(id=f"{self.id}_DFS_I", dirigido=False)  # El árbol DFS siempre es no dirigido

            # Agregar el nodo fuente al árbol DFS
            arbol_dfs.add_nodo(self.V[s.id])
            visitados.add(s.id)  # Marcar el nodo inicial como visitado

            while pila:
                nodo_actual_id = pila.pop()  # Obtener el ID del nodo actual
                nodo_actual = self.V[nodo_actual_id]  # Obtener el objeto Node

                for arista in self.E.values():
                    if arista.u.id == nodo_actual_id and arista.v.id not in visitados:
                        arbol_dfs.add_nodo(self.V[arista.v.id])
                        arbol_dfs.add_arista(Edge(self.V[arista.u.id], self.V[arista.v.id]))
                        pila.append(arista.v.id)
                        visitados.add(arista.v.id)  # Marcar el nodo vecino como visitado
                    elif arista.v.id == nodo_actual_id and arista.u.id not in visitados:  # Siempre revisa la otra dirección
                        arbol_dfs.add_nodo(self.V[arista.u.id])
                        arbol_dfs.add_arista(Edge(self.V[arista.v.id], self.V[arista.u.id]))
                        pila.append(arista.u.id)
                        visitados.add(arista.u.id)  # Marcar el nodo vecino como visitado

            return arbol_dfs
    
    def Dijkstra(self, s):
            """
            Crea un nuevo grafo de tipo árbol mediante el algoritmo de Dijkstra,
            que encuentra el grafo del camino más corto entre nodos
            Usa una función recursiva

            Parametros
            s : Nodo nodo raíz del árbol que se va a generar

            Returns
            tree : Grafo árbol generado
            """
            tree = Graph(id=f"{self.id}_Dijkstra")
            line = heapdict.heapdict()
            parents = dict()
            in_tree = set()

            line[s] = 0
            parents[s] = None
            for node in self.V:
                if node == s:
                    continue
                line[node] = np.inf
                parents[node] = None

            while line:
                u, u_dist = line.popitem()
                if u_dist == np.inf:
                    continue

                self.V[u].attrs['dist'] = u_dist
                tree.add_nodo(self.V[u])
                if parents[u] is not None:
                    arista = Edge(self.V[parents[u]], self.V[u])
                    tree.add_arista(arista)
                in_tree.add(u)

                # Obnetener los vecinos
                neighbor = []
                for arista in self.E:
                    if self.V[u].id in arista:
                        v = arista[0] if self.V[u].id == arista[1] else arista[1]
                        if v not in in_tree:
                            neighbor.append(v)

                # Actualizar distancias
                for v in neighbor:
                    arista = (u, v) if (u, v) in self.E else (v, u)
                    if line[v] > u_dist + self.E[arista].attrs['weight']:
                        line[v] = u_dist + self.E[arista].attrs['weight']
                        parents[v] = u

            return tree

    def KruskalD(self):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo de Kruskal
        directo, que encuentra el árbol de expansión mínima

        Returns
        -------
        mst : Grafo
            árbol de expansión mínima (mst)
        """

        mst = Graph(id=f"{self.id}_KruskalD")

        # Ordena aristas por peso
        edges_sorted = list(self.E.values())
        edges_sorted.sort(key = lambda edge: edge.attrs['weight'])

        # Componente conectada
        connected_comp = dict()
        for nodo in self.V:
            connected_comp[nodo] = nodo

        # Añadir aristas, iterando por peso
        for edge in edges_sorted:
            u, v = edge.u, edge.v
            if connected_comp[u.id] != connected_comp[v.id]:
                # Añade nodos y aristas al mst
                mst.add_nodo(u)
                mst.add_nodo(v)
                mst.add_arista(edge)

                # Cambia la componente conectada de v para que sea la misma que u
                for comp in connected_comp:
                    if connected_comp[comp] == connected_comp[v.id]:
                        other_comp = connected_comp[v.id]
                        connected_comp[comp] = connected_comp[u.id]

                        # Si se cambia la componente conectada de un nodo,
                        # cambiarla para toda la componente conectada
                        iterator = (key for key in connected_comp \
                                    if connected_comp[key] == other_comp)
                        for item in iterator:
                            connected_comp[item] = connected_comp[u.id]

        return mst


    def KruskalI(self):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo de Kruskal
        inverso, que encuentra el árbol de expansión mínima

        Returns
        -------
        mst : Grafo
            árbol de expansión mínima (mst)
        """
        mst = self.clone() 
        mst.id = f"{self.id}_KruskalI" # Actualizar el ID del grafo clonado

        # Ordena aristas por peso
        edges_sorted = list(self.E.values())
        edges_sorted.sort(key = lambda edge: edge.attrs['weight'], reverse=True)

        # Elimina aristas del mst
        for edge in edges_sorted:
            u, v = edge.u.id, edge.v.id
            # Verifica si la arista existe en mst.E antes de intentar eliminarla
            if (u, v) in mst.E:
                del(mst.E[(u, v)])
            elif (v, u) in mst.E: # Para grafos no dirigidos, verifica también la dirección inversa
                del(mst.E[(v, u)])
            else:
                continue # Arista no encontrada

            # Si el grafo no está conectado después de la eliminación, volver a colocar la arista
            # Verificar si mst.V está vacío antes de llamar a BFS
            if not mst.V or len(mst.BFS(self.V[edge.u.id]).V) != len(mst.V): 
                # Volver a colocar la arista. Asegurarse de que la arista se añada con su dirección/clave original
                # Esto asume que edge.id es una tupla (u.id, v.id) o (v.id, u.id)
                mst.add_arista(edge) # Usar add_arista para manejar tanto dirigido/no dirigido

        return mst


    def Prim(self):
        """
        Crea un nuevo grafo de tipo árbol mediante el algoritmo de Prim,
        que encuentra el árbol de expansión mínima

        Returns
        -------
        mst : Grafo
            árbol de expansión mínima (mst)
        """
        mst = Graph(id=f"{self.id}_Prim")
        line = heapdict.heapdict()
        parents = dict()
        in_tree = set()

        s = random.choice(list(self.V.values()))

        """
        Asignar valores infinitos a los nodos.
        Asignar nodo padre en el árbol a None.
        """
        line[s.id] = 0
        parents[s.id] = None
        for node in self.V:
            if node == s.id:
                continue
            line[node] = np.inf
            parents[node] = None

        while line:
            u, u_dist = line.popitem()
            if u_dist == np.inf:
                continue

            self.V[u].attrs['dist'] = u_dist
            mst.add_nodo(self.V[u])
            if parents[u] is not None:
                # Crea una arista desde el padre al nodo actual
                arista = Edge(self.V[parents[u]], self.V[u]) 
                # Encuentra el peso de las aristas del grafo original
                if (u, parents[u]) in self.E:
                    weight = self.E[(u, parents[u])].attrs['weight']
                elif (parents[u], u) in self.E: # Verificar para grafo no dirigido
                    weight = self.E[(parents[u], u)].attrs['weight']
                else:
                    weight = 0 # Valor por defecto o si la arista no se encuentra
                arista.attrs['weight'] = weight
                mst.add_arista(arista)
            in_tree.add(u)

            # Obtener nodos vecinos
            neigh = []
            for arista_id in self.E: # Itera sobre las claves (tuplas)
                # Verifica si el nodo actual 'u' es parte de la arista
                if self.V[u].id == arista_id[0]:
                    v = arista_id[1]
                elif self.V[u].id == arista_id[1]:
                    v = arista_id[0]
                else:
                    continue # No conectado a 'u'

                if v not in in_tree: #Verifica que 'v' no esté ya en el árbol
                    # Añade el vecino a la lista de vecinos
                    neigh.append(v)

            # Actualiza las distancias
            for v in neigh:
                arista_key = (u, v) if (u, v) in self.E else (v, u)
                if line[v] > self.E[arista_key].attrs['weight']:
                    line[v] = self.E[arista_key].attrs['weight'] 
                    parents[v] = u #Actualiza el padre del nodo vecino

        return mst