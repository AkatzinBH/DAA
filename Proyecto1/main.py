import random
from algoritmos import grafoMalla
from algoritmos import grafoErdosRenyi
from algoritmos import grafoGilbert
from algoritmos import grafoGeografico
from algoritmos import grafoBarabasiAlbert
from algoritmos import grafoDorogovtsevMendes

def main():
    nodos = 500
    nodos_malla_mn = (25, 20)
    aristas_Erdos = random.randint(nodos-1,3*(nodos-1))
    p_Gilbert = 0.25
    r_Geografico = 0.3
    d_Barabasi = 7

    # Crear un grafo de malla
    grafo = grafoMalla(*nodos_malla_mn)
    grafo.to_graphviz(grafo.id + ".gv")

    # Crear un grafo Erdos-Renyi
    grafo = grafoErdosRenyi(nodos, aristas_Erdos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")

    # Crear un grafo Gilbert
    grafo = grafoGilbert(nodos, p_Gilbert, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")

    # Crear un grafo geográfico simple
    grafo = grafoGeografico(nodos, r_Geografico, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")

    # Crear un grafo Barabasi-Albert
    grafo = grafoBarabasiAlbert(nodos, d_Barabasi, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")

    #Crear un grafo Dorogovtsev-Mendes
    grafo = grafoDorogovtsevMendes(nodos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")

if __name__ == "__main__":
    main()