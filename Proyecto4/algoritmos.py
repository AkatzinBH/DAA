import sys
import random
from node import Node
from edge import Edge
from graph import Graph

def grafoMalla(m, n, dirigido=False):
    """
    Genera un grafo de malla con IDs de nodo enteros.
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if m < 2 or n < 2:
        print("Error. m y n, deben ser mayores que 1", file=sys.stderr)
        exit(-1)

    grafo = Graph(id=f"grafoMalla_{m}_{n}", dirigido=dirigido)
    nodos = {}
    
    # Crear nodos con IDs enteros
    contador_id_nodo = 0  # Inicializar un contador para los IDs
    for i in range(m):
        for j in range(n):
            nodo = Node(contador_id_nodo)  # Usar el contador como ID
            nodos[(i, j)] = nodo
            grafo.add_nodo(nodo)
            contador_id_nodo += 1  # Incrementar el contador

    # Crear aristas
    for i in range(m):
        for j in range(n):
            id_nodo_actual = i * n + j  # Calcular el ID del nodo actual
            if i < m - 1:  # Arista hacia el nodo de abajo
                id_vecino_abajo = (i + 1) * n + j
                grafo.add_arista(Edge(nodos[(i, j)], nodos[(i + 1, j)]))
            if j < n - 1:  # Arista hacia el nodo de la derecha
                id_vecino_derecha = i * n + (j + 1)
                grafo.add_arista(Edge(nodos[(i, j)], nodos[(i, j + 1)]))

    return grafo

def grafoErdosRenyi(n, m, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if n <= 0:
        print("Error. n debe ser mayor que 0", file=sys.stderr)
        exit(-1)
    if m < n - 1:
        print("Error. m debe ser al menos n-1 para garantizar conectividad", file=sys.stderr)
        exit(-1)
    if m > n * (n - 1) // (1 if dirigido else 2):
        print("Error. m excede el número máximo de aristas posibles", file=sys.stderr)
        exit(-1)

    grafo = Graph(id=f"grafoErdosRenyi_{n}_{m}", dirigido=dirigido)
    nodos = {}

    # Crear nodos
    for i in range(n):
        nodo = Node(i)
        nodos[i] = nodo
        grafo.add_nodo(nodo)

    # Crear aristas aleatorias
    posibles_aristas = [(u, v) for u in range(n) for v in range(n) if u != v]
    if not dirigido:
        posibles_aristas = [(u, v) for u, v in posibles_aristas if u < v]

    aristas_seleccionadas = random.sample(posibles_aristas, m)
    for u, v in aristas_seleccionadas:
        grafo.add_arista(Edge(nodos[u], nodos[v]))

    return grafo

def grafoGilbert(n, p, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if n <= 0:
        print("Error. n debe ser mayor que 0", file=sys.stderr)
        exit(-1)
    if not (0 <= p <= 1):
        print("Error. p debe estar en el rango [0, 1]", file=sys.stderr)
        exit(-1)

    grafo = Graph(id=f"grafoGilbert_{n}_{p}", dirigido=dirigido)
    nodos = {}

    # Crear nodos
    for i in range(n):
        nodo = Node(i)
        nodos[i] = nodo
        grafo.add_nodo(nodo)

    # Crear aristas con probabilidad p
    for u in range(n):
        for v in range(n):
            # Evitar bucles y duplicados en grafos no dirigidos
            if u != v and (dirigido or u < v):
                # Crear arista con probabilidad p
                if random.random() <= p:
                    grafo.add_arista(Edge(nodos[u], nodos[v]))

    return grafo

def grafoGeografico(n, r, dirigido=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple
    Colocar n nodos en un rectángulo unitario con coordenadas uniformes (o normales)
    y colocar una arista entre cada par que queda en distancia r o menor.
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear un nodo (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if r > 1 or r < 0 or n < 1:
        print("Error: 0 <= r <= 1 y n > 0", file=sys.stderr)
        exit(-1)

    coords = dict()
    grafo = Graph(id=f"grafoGeografico_{n}_{int(r * 100)}", dirigido=dirigido)
    nodos = grafo.V

    # Crear nodos
    for nodo in range(n):
        grafo.add_nodo(Node(nodo))
        x = round(random.random(), 3)
        y = round(random.random(), 3)
        coords[nodo] = (x, y)

    # Crear aristas
    r **= 2
    for u in nodos:
        vs = (v for v in nodos if u != v)
        # Se agregan los nodos dentro de la distancia r
        for v in vs:
            dist = (coords[u][0] - coords[v][0]) ** 2 \
                    + (coords[u][1] - coords[v][1]) ** 2
            if dist <= r:
                grafo.add_arista(Edge(nodos[u], nodos[v]))

    return grafo

def grafoBarabasiAlbert(n, d, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if n < 1 or d < 2:
        print("Error: n > 0 y d > 1", file=sys.stderr)
        exit(-1)

    grafo = Graph(id=f"grafoBarabasi_{n}_{d}", dirigido=dirigido)
    nodos = grafo.V
    grado_nodo = dict()

    # Crear nodos
    for nodo in range(n):
        grafo.add_nodo(Node(nodo))
        grado_nodo[nodo] = 0

    # Agregar aristas al azar
    for nodo in nodos:
        for v in nodos:
            if grado_nodo[nodo] == d:
                break
            if grado_nodo[v] == d:
                continue
            p = random.random()
            equal_nodes = v == nodo
            if equal_nodes:
                continue

            if p <= 1 - grado_nodo[v] / d and grafo.add_arista(Edge(nodos[nodo], nodos[v])):
                grado_nodo[nodo] += 1
                if not equal_nodes:
                    grado_nodo[v] += 1

    return grafo

def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Dorogovtsev-Mendes
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if n < 3:
        print("Error: n debe ser mayor o igual a 3", file=sys.stderr)
        exit(-1)

    grafo = Graph(id=f"grafoDorogovtsevMendes_{n}", dirigido=dirigido)
    nodos = {}
    aristas = []

    # Crear los 3 nodos iniciales y conectarlos formando un triángulo
    for i in range(3):
        nodo = Node(i)
        nodos[i] = nodo
        grafo.add_nodo(nodo)

    grafo.add_arista(Edge(nodos[0], nodos[1]))
    grafo.add_arista(Edge(nodos[1], nodos[2]))
    grafo.add_arista(Edge(nodos[2], nodos[0]))

    aristas.append((nodos[0], nodos[1]))
    aristas.append((nodos[1], nodos[2]))
    aristas.append((nodos[2], nodos[0]))

    # Agregar los nodos restantes
    for i in range(3, n):
        nuevo_nodo = Node(i)
        nodos[i] = nuevo_nodo
        grafo.add_nodo(nuevo_nodo)

        # Seleccionar una arista al azar
        u, v = random.choice(aristas)

        # Conectar el nuevo nodo a los extremos de la arista seleccionada
        grafo.add_arista(Edge(nuevo_nodo, u))
        grafo.add_arista(Edge(nuevo_nodo, v))

        if not dirigido:
            grafo.add_arista(Edge(u, nuevo_nodo))
            grafo.add_arista(Edge(v, nuevo_nodo))

        # Agregar las nuevas aristas a la lista de aristas
        aristas.append((nuevo_nodo, u))
        aristas.append((nuevo_nodo, v))

    return grafo