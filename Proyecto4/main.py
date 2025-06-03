import random
from algoritmos import grafoMalla
from algoritmos import grafoErdosRenyi
from algoritmos import grafoGilbert
from algoritmos import grafoGeografico
from algoritmos import grafoBarabasiAlbert
from algoritmos import grafoDorogovtsevMendes
from node import Node

def main():
    nodos = 300
    nodos_malla_mn = (20, 15)
    aristas_Erdos = nodos*4
    p_Gilbert = 0.25
    r_Geografico = 0.3
    d_Barabasi = 7
    
    # Crear un grafo de malla
    grafo = grafoMalla(*nodos_malla_mn)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.random_weights()
    kruskal = grafo.KruskalD()
    kruskal.to_graphviz(kruskal.id + ".gv")
    kruskalI = grafo.KruskalI()
    kruskalI.to_graphviz(kruskalI.id + ".gv")
    prim = grafo.Prim()
    prim.to_graphviz(prim.id + ".gv")
    print(f"costo kruskal (Malla): {kruskal.costo()}")
    print(f"costo kruskalI (Malla): {kruskalI.costo()}")
    print(f"costo prim (Malla): {prim.costo()}")

    # Crear un grafo Erdos-Renyi
    grafo = grafoErdosRenyi(nodos, aristas_Erdos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.random_weights()
    kruskal = grafo.KruskalD()
    kruskal.to_graphviz(kruskal.id + ".gv")
    kruskalI = grafo.KruskalI()
    kruskalI.to_graphviz(kruskalI.id + ".gv")
    prim = grafo.Prim()
    prim.to_graphviz(prim.id + ".gv")
    print(f"costo kruskal (Erdos-Renyi): {kruskal.costo()}")
    print(f"costo kruskalI (Erdos-Renyi): {kruskalI.costo()}")
    print(f"costo prim (Erdos-Renyi): {prim.costo()}")

    # Crear un grafo Gilbert
    grafo = grafoGilbert(nodos, p_Gilbert, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.random_weights()
    kruskal = grafo.KruskalD()
    kruskal.to_graphviz(kruskal.id + ".gv")
    kruskalI = grafo.KruskalI()
    kruskalI.to_graphviz(kruskalI.id + ".gv")
    prim = grafo.Prim()
    prim.to_graphviz(prim.id + ".gv")
    print(f"costo kruskal (Gilbert): {kruskal.costo()}")
    print(f"costo kruskalI (Gilbert): {kruskalI.costo()}")
    print(f"costo prim (Gilbert): {prim.costo()}")

    # Crear un grafo geográfico simple
    grafo = grafoGeografico(nodos, r_Geografico, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.random_weights()
    kruskal = grafo.KruskalD()
    kruskal.to_graphviz(kruskal.id + ".gv")
    kruskalI = grafo.KruskalI()
    kruskalI.to_graphviz(kruskalI.id + ".gv")
    prim = grafo.Prim()
    prim.to_graphviz(prim.id + ".gv")
    print(f"costo kruskal (Geografico): {kruskal.costo()}")
    print(f"costo kruskalI (Geografico): {kruskalI.costo()}")
    print(f"costo prim (Geografico): {prim.costo()}")

    # Crear un grafo Barabasi-Albert
    grafo = grafoBarabasiAlbert(nodos, d_Barabasi, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.random_weights()
    kruskal = grafo.KruskalD()
    kruskal.to_graphviz(kruskal.id + ".gv")
    kruskalI = grafo.KruskalI()
    kruskalI.to_graphviz(kruskalI.id + ".gv")
    prim = grafo.Prim()
    prim.to_graphviz(prim.id + ".gv")
    print(f"costo kruskal (Barabasi-Albert): {kruskal.costo()}")
    print(f"costo kruskalI (Barabasi-Albert): {kruskalI.costo()}")
    print(f"costo prim (Barabasi-Albert): {prim.costo()}")

    # Crear un grafo Dorogovtsev-Mendes
    grafo = grafoDorogovtsevMendes(nodos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    grafo.random_weights()
    kruskal = grafo.KruskalD()
    kruskal.to_graphviz(kruskal.id + ".gv")
    kruskalI = grafo.KruskalI()
    kruskalI.to_graphviz(kruskalI.id + ".gv")
    prim = grafo.Prim()
    prim.to_graphviz(prim.id + ".gv")
    print(f"costo kruskal (Dorogovtsev-Mendes): {kruskal.costo()}")
    print(f"costo kruskalI (Dorogovtsev-Mendes): {kruskalI.costo()}")
    print(f"costo prim (Dorogovtsev-Mendes): {prim.costo()}")

if __name__ == "__main__":
    main()