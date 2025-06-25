import random
from algoritmos import grafoMalla
from algoritmos import grafoErdosRenyi
from algoritmos import grafoGilbert
from algoritmos import grafoGeografico
from algoritmos import grafoBarabasiAlbert
from algoritmos import grafoDorogovtsevMendes
from node import Node
from Visualizer import spring
from Visualizer import fruchterman_reginold

def main():
    nodos = 500
    nodos_malla_mn = (25, 20)
    aristas_Erdos = nodos*4
    p_Gilbert = 0.1
    r_Geografico = 0.3
    d_Barabasi = 7
    
    """
    print("Grafo Malla")
    grafo = grafoMalla(*nodos_malla_mn)
    fruchterman_reginold(grafo,fuerza=0.25)

    print("Grafo Erdos-Renyi")
    grafo = grafoErdosRenyi(nodos, aristas_Erdos)
    fruchterman_reginold(grafo, fuerza=0.4)

    print("Grafo Gilbert")
    grafo = grafoGilbert(nodos, p_Gilbert)
    fruchterman_reginold(grafo, fuerza=3)

    print("Grafo Geografico")
    grafo = grafoGeografico(nodos, r_Geografico)
    fruchterman_reginold(grafo, fuerza=3)

    print("Grafo Barabasi-Albert")
    grafo = grafoBarabasiAlbert(nodos, d_Barabasi, dirigido=False)
    fruchterman_reginold(grafo, fuerza=1)
"""
    print("Grafo Dorogovtsev-Mendes")
    grafo = grafoDorogovtsevMendes(nodos)
    fruchterman_reginold(grafo, fuerza=0.3)
    
if __name__ == "__main__":
    main()