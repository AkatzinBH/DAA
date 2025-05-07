import random
from algoritmos import grafoMalla
from algoritmos import grafoErdosRenyi
from algoritmos import grafoGilbert
from algoritmos import grafoGeografico
from algoritmos import grafoBarabasiAlbert
from algoritmos import grafoDorogovtsevMendes

def main():
    nodos = 500 #30,100,500
    nodos_malla_mn = (25, 20)
    aristas_Erdos = nodos*4
    p_Gilbert = 0.25
    r_Geografico = 0.3
    d_Barabasi = 7

    # Crear un grafo de malla
    grafo = grafoMalla(*nodos_malla_mn)
    grafo.to_graphviz(grafo.id + ".gv")

    # Crear un grafo de malla con BFS
    bfs = grafo.BFS((0,0))
    bfs.to_graphviz(bfs.id + ".gv")
    # Crear un grafo de malla con DFS Recursivo
    dfs_r = grafo.DFS_R((0,0))
    dfs_r.to_graphviz(dfs_r.id + ".gv")
    # Crear un grafo de malla con DFS Iterativo
    dfs_i = grafo.DFS_I((0,0))
    dfs_i.to_graphviz(dfs_i.id + ".gv")

    # Crear un grafo Erdos-Renyi
    grafo = grafoErdosRenyi(nodos, aristas_Erdos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    # Crear un grafo Erdos-Renyi con BFS
    bfs = grafo.BFS(0)
    bfs.to_graphviz(bfs.id + ".gv")
    # Crear un grafo Erdos-Renyi con DFS Recursivo
    dfs_r = grafo.DFS_R(0)
    dfs_r.to_graphviz(dfs_r.id + ".gv")
    # Crear un grafo Erdos-Renyi con DFS Iterativo
    dfs_i = grafo.DFS_I(0)
    dfs_i.to_graphviz(dfs_i.id + ".gv")

    # Crear un grafo Gilbert
    grafo = grafoGilbert(nodos, p_Gilbert, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    # Crear un grafo Gilbert con BFS
    bfs = grafo.BFS(0)
    bfs.to_graphviz(bfs.id + ".gv")
    # Crear un grafo Gilbert con DFS Recursivo
    dfs_r = grafo.DFS_R(0)
    dfs_r.to_graphviz(dfs_r.id + ".gv")
    # Crear un grafo Gilbert con DFS Iterativo
    dfs_i = grafo.DFS_I(0)
    dfs_i.to_graphviz(dfs_i.id + ".gv")

    # Crear un grafo geográfico simple
    grafo = grafoGeografico(nodos, r_Geografico, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    # Crear un grafo geográfico simple con BFS
    bfs = grafo.BFS(0)
    bfs.to_graphviz(bfs.id + ".gv")
    # Crear un grafo geográfico simple con DFS Recursivo
    dfs_r = grafo.DFS_R(0)
    dfs_r.to_graphviz(dfs_r.id + ".gv")
    # Crear un grafo geográfico simple con DFS Iterativo
    dfs_i = grafo.DFS_I(0)
    dfs_i.to_graphviz(dfs_i.id + ".gv")

    # Crear un grafo Barabasi-Albert
    grafo = grafoBarabasiAlbert(nodos, d_Barabasi, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    # Crear un grafo Barabasi-Albert con BFS
    bfs = grafo.BFS(0)
    bfs.to_graphviz(bfs.id + ".gv")
    # Crear un grafo Barabasi-Albert con DFS Recursivo
    dfs_r = grafo.DFS_R(0)
    dfs_r.to_graphviz(dfs_r.id + ".gv")
    # Crear un grafo Barabasi-Albert con DFS Iterativo
    dfs_i = grafo.DFS_I(0)
    dfs_i.to_graphviz(dfs_i.id + ".gv")

    #Crear un grafo Dorogovtsev-Mendes
    grafo = grafoDorogovtsevMendes(nodos, dirigido=False)
    grafo.to_graphviz(grafo.id + ".gv")
    # Crear un grafo Dorogovtsev-Mendes con BFS
    bfs = grafo.BFS(0)
    bfs.to_graphviz(bfs.id + ".gv")
    # Crear un grafo Dorogovtsev-Mendes con DFS Recursivo
    dfs_r = grafo.DFS_R(0)
    dfs_r.to_graphviz(dfs_r.id + ".gv")
    # Crear un grafo Dorogovtsev-Mendes con DFS Iterativo
    dfs_i = grafo.DFS_I(0)
    dfs_i.to_graphviz(dfs_i.id + ".gv")

if __name__ == "__main__":
    main()