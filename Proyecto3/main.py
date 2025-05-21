import random
from algoritmos import grafoMalla
from algoritmos import grafoErdosRenyi
from algoritmos import grafoGilbert
from algoritmos import grafoGeografico
from algoritmos import grafoBarabasiAlbert
from algoritmos import grafoDorogovtsevMendes
from node import Node

def main():
    nodos = 500
    nodos_malla_mn = (25, 20)
    aristas_Erdos = nodos*4
    p_Gilbert = 0.25
    r_Geografico = 0.3
    d_Barabasi = 7
    
    # Crear un grafo de malla
    print("Creando grafo de malla")
    grafo = grafoMalla(*nodos_malla_mn)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.equal_weights()
    dijkstra = grafo.Dijkstra(0)
    dijkstra.to_graphviz(dijkstra.id + ".gv")
    print(f"g_nodes: {len(grafo.V)}")
    print(f"dijkstra_nodes: {len(dijkstra.V)}")

    # Crear un grafo Erdos-Renyi
    print("Creando grafo Erdos-Renyi")
    grafo = grafoErdosRenyi(nodos, aristas_Erdos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.equal_weights()
    dijkstra = grafo.Dijkstra(0)
    dijkstra.to_graphviz(dijkstra.id + ".gv")
    print(f"g_nodes (Erdos-Renyi): {len(grafo.V)}")
    print(f"dijkstra_nodes (Erdos-Renyi): {len(dijkstra.V)}")

    # Crear un grafo Gilbert
    print("Creando grafo Gilbert")
    grafo = grafoGilbert(nodos, p_Gilbert, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.equal_weights()
    dijkstra = grafo.Dijkstra(0)
    dijkstra.to_graphviz(dijkstra.id + ".gv")
    print(f"g_nodes (Gilbert): {len(grafo.V)}")
    print(f"dijkstra_nodes (Gilbert): {len(dijkstra.V)}")

    # Crear un grafo geográfico simple
    print("Creando grafo geográfico simple")
    grafo = grafoGeografico(nodos, r_Geografico, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.equal_weights()
    dijkstra = grafo.Dijkstra(0)
    dijkstra.to_graphviz(dijkstra.id + ".gv")
    print(f"g_nodes (Geografico): {len(grafo.V)}")
    print(f"dijkstra_nodes (Geografico): {len(dijkstra.V)}")

    # Crear un grafo Barabasi-Albert
    print("Creando grafo Barabasi-Albert")
    grafo = grafoBarabasiAlbert(nodos, d_Barabasi, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.equal_weights()
    dijkstra = grafo.Dijkstra(0)
    dijkstra.to_graphviz(dijkstra.id + ".gv")
    print(f"g_nodes (Barabasi-Albert): {len(grafo.V)}")
    print(f"dijkstra_nodes (Barabasi-Albert): {len(dijkstra.V)}")
    
    # Crear un grafo Dorogovtsev-Mendes
    print("Creando grafo Dorogovtsev-Mendes")
    grafo = grafoDorogovtsevMendes(nodos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.equal_weights()
    dijkstra = grafo.Dijkstra(0)
    dijkstra.to_graphviz(dijkstra.id + ".gv")
    print(f"g_nodes (Dorogovtsev-Mendes): {len(grafo.V)}")
    print(f"dijkstra_nodes (Dorogovtsev-Mendes): {len(dijkstra.V)}")

if __name__ == "__main__":
    main()