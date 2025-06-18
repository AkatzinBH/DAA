import random
from algoritmos import grafoMalla
from algoritmos import grafoErdosRenyi
from algoritmos import grafoGilbert
from algoritmos import grafoGeografico
from algoritmos import grafoBarabasiAlbert
from algoritmos import grafoDorogovtsevMendes
from node import Node
from eades import spring

def main():
    nodos = 100
    nodos_malla_mn = (10, 10)
    aristas_Erdos = nodos*4
    p_Gilbert = 0.25
    r_Geografico = 0.3
    d_Barabasi = 7
    
    """
    print("Grafo Malla")
    grafo = grafoMalla(*nodos_malla_mn)
    spring(grafo)

    print("Grafico Erdos-Renyi")
    grafo = grafoErdosRenyi(nodos, aristas_Erdos)
    spring(grafo)

    print("Grafico Gilbert")
    grafo = grafoGilbert(nodos, p_Gilbert)
    spring(grafo)

    print("Grafico Geografico")
    grafo = grafoGeografico(nodos, r_Geografico)
    spring(grafo)
"""
    print("Grafico Barabasi-Albert")
    grafo = grafoBarabasiAlbert(nodos, d_Barabasi, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    spring(grafo)
"""
    print("Grafico Dorogovtsev-Mendes")
    grafo = grafoDorogovtsevMendes(nodos)
    spring(grafo)
"""
if __name__ == "__main__":
    main()