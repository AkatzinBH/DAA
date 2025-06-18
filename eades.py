from math import log, atan2, cos, sin
import pygame
import random

from edge import Edge
from graph  import Graph
from node  import Node

# Configuración de la ventana principal
WIDTH, HEIGHT   = 1920, 1080
BORDER          = 15
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores
BG              = (255, 255, 255)
GRAY            = (128, 128, 128)
BLACK           = (40, 40, 40)
CYAN             = (0, 128, 128)

# Configuración de la simulación
ITERS           = 300
FPS             = 65
NODE_RADIUS     = 7
DIST_MIN        = (min(WIDTH, HEIGHT)) // 35
NODE_MIN_WIDTH  = 25
NODE_MIN_HEIGHT = 25
NODE_MAX_WIDTH  = WIDTH - 25
NODE_MAX_HEIGHT = HEIGHT - 25

# Parámetros de la simulación
#Ajustar valores dependiendo del grafo
c1 = 1.5 
c2 = 1 
c3 = 0.5 
c4 = 1 


def spring(g):
    """
    Muestra una animación del método de visualización "spring" de Eades.

    Parámetros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualización
    """

    run = True
    clock = pygame.time.Clock()

    init_nodes(g)
    # Las llamadas a draw_edges y draw_nodes iniciales se hacen dentro del bucle principal
    # para que se actualicen en cada iteración.

    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if i > ITERS:
            # Si las iteraciones han terminado, la ventana permanecerá abierta,
            # pero la simulación de fuerzas se detendrá.
            continue 

        WIN.fill(BG)
        update_nodes(g)
        draw_edges(g)
        draw_nodes(g)
        pygame.display.update()
        i += 1

    pygame.quit()
    return


def init_nodes(g):
    """
    Inicializa los nodos del grafo g en posiciones aleatorias.

    Parámetros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualización
    """

    for node in g.V.values():
        x = random.randrange(NODE_MIN_WIDTH, NODE_MAX_WIDTH)
        y = random.randrange(NODE_MIN_HEIGHT, NODE_MAX_HEIGHT)
        node.attrs['coords'] = [x, y]

    return

def update_nodes(g):
    """
    Aplica la fuerza a los nodos del grafo G para actualizar su posición.

    Parámetros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualización
    """
    ################
    for node in g.V.values():
        x_attraction = 0
        y_attraction = 0
        x_node, y_node = node.attrs['coords']

        for other in node.connected_to:
            x_other, y_other = g.V[other].attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5

            # Definiendo la distancia mínima
            if d < DIST_MIN:
                continue
            attraction = c1 * log(d / c2)
            angle = atan2(y_other - y_node, x_other - x_node)
            x_attraction += attraction * cos(angle)
            y_attraction += attraction * sin(angle)

        not_connected = (other for other in g.V.values()
                            if (other.id not in node.connected_to and other != node))
        x_repulsion = 0
        y_repulsion = 0
        for other in not_connected:
            x_other, y_other = other.attrs['coords']
            d = ((x_node - x_other) ** 2 + (y_node - y_other)**2) ** 0.5
            if d == 0:
                continue
            repulsion = c3 / d ** 0.5
            angle = atan2(y_other - y_node, x_other - x_node)
            x_repulsion -= repulsion * cos(angle)
            y_repulsion -= repulsion * sin(angle)

        fx = x_attraction + x_repulsion
        fy = y_attraction + y_repulsion
        node.attrs['coords'][0] += c4 * fx
        node.attrs['coords'][1] += c4 * fy

        # Restringir por los límites de la ventana
        node.attrs['coords'][0] = max(node.attrs['coords'][0], NODE_MIN_WIDTH)
        node.attrs['coords'][1] = max(node.attrs['coords'][1], NODE_MIN_HEIGHT)
        node.attrs['coords'][0] = min(node.attrs['coords'][0], NODE_MAX_WIDTH)
        node.attrs['coords'][1] = min(node.attrs['coords'][1], NODE_MAX_HEIGHT)

    return


def draw_nodes(g):
    """
    Dibuja los nodos del grafo g.

    Parámetros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualización
    """

    for node in g.V.values():
        pygame.draw.circle(WIN, GRAY, node.attrs['coords'], NODE_RADIUS - 3, 0)
        pygame.draw.circle(WIN, CYAN, node.attrs['coords'], NODE_RADIUS, 3)

    return


def draw_edges(g):
    """
    Dibuja las aristas del grafo g.

    Parámetros
    ----------
    g : Grafo
        grafo para el cual se realiza la visualización
    """

    for edge in g.E:
        u, v = edge
        u_pos = g.V[u].attrs['coords']
        v_pos = g.V[v].attrs['coords']

        pygame.draw.line(WIN, BLACK, u_pos, v_pos, 1)

    return
