from node import Node
from edge import Edge

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
    