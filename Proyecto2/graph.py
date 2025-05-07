from node import Node
from edge import Edge
import sys

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
        
    def to_graphviz(self, filename):
        edge_connector = "--"
        graph_directive = "graph"
        if self.dirigido:
            edge_connector = "->"
            graph_directive = "digraph"

        with open(filename, 'w') as f:
            f.write(f"{graph_directive} {self.id} " + " {\n")
            for nodo in self.V.values():
                # Verificar si el id del nodo es una tupla o un entero
                if isinstance(nodo.id, tuple):
                    f.write(f"n_{nodo.id[0]}_{nodo.id[1]};\n")
                else:
                    f.write(f"n_{nodo.id};\n")
            for arista in self.E.values():
                # Verificar si los ids de los nodos son tuplas o enteros
                if isinstance(arista.u.id, tuple) and isinstance(arista.v.id, tuple):
                    f.write(f"n_{arista.u.id[0]}_{arista.u.id[1]} {edge_connector} n_{arista.v.id[0]}_{arista.v.id[1]};\n")
                else:
                    f.write(f"n_{arista.u.id} {edge_connector} n_{arista.v.id};\n")
            f.write("}")

    def BFS(self, s):
            """
            Realiza una búsqueda en anchura (BFS) desde el nodo fuente s.
            :param s: Nodo fuente
            :return: Un nuevo grafo que representa el árbol BFS
            """
            if s not in self.V:
                print("Error: El nodo fuente no existe en el grafo.", file=sys.stderr)
                return None

            visitados = set()
            cola = [s]
            arbol_bfs = Graph(id=f"{self.id}_BFS", dirigido=self.dirigido)

            # Agregar el nodo fuente al árbol BFS
            arbol_bfs.add_nodo(self.V[s])

            while cola:
                nodo_actual = cola.pop(0)
                visitados.add(nodo_actual)

                for arista in self.E.values():
                    if arista.u.id == nodo_actual and arista.v.id not in visitados:
                        arbol_bfs.add_nodo(self.V[arista.v.id])
                        arbol_bfs.add_arista(Edge(self.V[arista.u.id], self.V[arista.v.id]))
                        cola.append(arista.v.id)
                        visitados.add(arista.v.id)

            return arbol_bfs

    def DFS_R(self, s):
        """
        Realiza una búsqueda en profundidad recursiva (DFS) desde el nodo fuente s.
        :param s: Nodo fuente
        :return: Un nuevo grafo que representa el árbol DFS
        """
        if s not in self.V:
            print("Error: El nodo fuente no existe en el grafo.", file=sys.stderr)
            return None

        visitados = set()
        arbol_dfs = Graph(id=f"{self.id}_DFS_R", dirigido=self.dirigido)

        def dfs_recursivo(nodo_actual):
            visitados.add(nodo_actual)
            arbol_dfs.add_nodo(self.V[nodo_actual])

            for arista in self.E.values():
                if arista.u.id == nodo_actual and arista.v.id not in visitados:
                    arbol_dfs.add_arista(Edge(self.V[arista.u.id], self.V[arista.v.id]))
                    dfs_recursivo(arista.v.id)

        dfs_recursivo(s)
        return arbol_dfs

    def DFS_I(self, s):
        """
        Realiza una búsqueda en profundidad iterativa (DFS) desde el nodo fuente s.
        :param s: Nodo fuente
        :return: Un nuevo grafo que representa el árbol DFS
        """
        if s not in self.V:
            print("Error: El nodo fuente no existe en el grafo.", file=sys.stderr)
            return None

        visitados = set()
        pila = [s]
        arbol_dfs = Graph(id=f"{self.id}_DFS_I", dirigido=self.dirigido)

        # Agregar el nodo fuente al árbol DFS
        arbol_dfs.add_nodo(self.V[s])

        while pila:
            nodo_actual = pila.pop()
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                for arista in self.E.values():
                    if arista.u.id == nodo_actual and arista.v.id not in visitados:
                        arbol_dfs.add_nodo(self.V[arista.v.id])
                        arbol_dfs.add_arista(Edge(self.V[arista.u.id], self.V[arista.v.id]))
                        pila.append(arista.v.id)

        return arbol_dfs