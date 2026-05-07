# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

import pygame
import sys

# Iniciar pygame
pygame.init()

# Tamaño ventana
pantalla = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Parque Pacman")

# Colores
NEGRO = (0, 0, 0)
AZUL = (100, 200, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Fuente
fuente = pygame.font.SysFont(None, 40)

pygame.display.flip()