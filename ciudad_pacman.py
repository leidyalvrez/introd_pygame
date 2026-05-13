# importamos la libreria pygame
import pygame
import sys
import math


# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((800,600))

# establecer titulo de la ventana
pygame.display.set_caption("Dibujar formas básicas")

# definición colores
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255, 165, 0)
verde = (0,255,0)
rosado =(255,192,203)


# variables auxiliares
PI = math.pi


# bucle principal del juego
while True:

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)
    

    # Lineas rectas continuas
    puntos_1 = [(400,600), (400,200), (200,200), (200,600)]
    pygame.draw.lines(ventana, rojo, False, puntos_1)

        # Circulo
    pygame.draw.circle(ventana, naranja, (300,300), 100, 1)

        # Texto 
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Leidy ", 1, azul)
    ventana.blit(texto, (250,280))

        # Texto 
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("PARQUE PACMAN ", 1, rosado)
    ventana.blit(texto, (325,90))


        # Arcos 
    pygame.draw.arc(ventana, verde, (200,0,200,200), PI/4, 7*PI/4,100)



    # actualizar visualización de la ventana
    pygame.display.flip()