# ----------------------------------------------------------- Librerías -----------------------------------------------------------------------

import numpy as np
import time
import random

# ----------------------------------------------------- Funciones -----------------------------------------------------------------------------

def crear_tablero(tamaño=(10, 10)): #Tablero vacio
    return np.full(tamaño, '_')

def colocar_barco(barco, tablero): 
    for (x, y) in barco:
        tablero[x, y] = "B"
    return tablero 

def tablero_maquina_base(tablero): #este tablero oculta los barcos de la maquina, solo muestra los disparos del 
    print("Tablero máquina")
    for fila in tablero:
        filasvisibles = []
        for casilla in fila:
            if casilla == "B":
                filasvisibles.append('_')
            else:
                filasvisibles.append(casilla)
        print(" ".join(filasvisibles))

def disparar(casilla, tablero):
    fila, columna = casilla

    if tablero[fila, columna] == "B":
        print("¡Acertaste!")
        print("   \\   |   /   ")
        print("-----O-----")
        print("   /  |  \\   ")
        print("    IMPACTO    ")
        tablero[fila, columna] = "X" #Reemplaza la B de barco por el disparo

    elif tablero[fila, columna] == '_':
        print("~~~~~~~~~~")
        print("~~¡Agua!~~")
        print("~~~~~~~~~~")
        tablero[fila, columna] = "A" #Si el disparo cae en agua

    else:
        print("Ya disparaste aquí.")  


def crear_barco(eslora, tablero):
    barco = [] #para almacenar posiciones del barco aleatorias, luego de generarse
    while len(barco) < eslora:
        x, y = random.randint(0, 9), random.randint(0, 9)  #genera las coordenadas de forma aleatoria
        if tablero[x, y] == '_':
            barco.append((x, y))
    return barco

def crear_barco_direccion(eslora, tablero, direccion):
    while True: 
        fila, columna = random.randint(0, 9), random.randint(0, 9) #genera las coordenadas de forma aleatoria
        barco = []  # Lista para almacenar las posiciones del barco

        if direccion == "norte" and fila - eslora + 1 >= 0:  #sube
            barco = [(fila - i, columna) for i in range(eslora)]
        elif direccion == "sur" and fila + eslora <= 10:  #baja
            barco = [(fila + i, columna) for i in range(eslora)]
        elif direccion == "este" and columna + eslora <= 10:  #derecha
            barco = [(fila, columna + i) for i in range(eslora)]
        elif direccion == "oeste" and columna - eslora + 1 >= 0:  #izquierda
            barco = [(fila, columna - i) for i in range(eslora)]
        else:
            continue #Si al generar el barco no entra en el tablero, se genera nuevamente, asi hasta que entre en el tablero

        if all(tablero[pos[0], pos[1]] == '_' for pos in barco): #verifica si no hay otro barco en esa posicion generada
            return barco 
        
def ganar(tablero):
    return not np.any(tablero == "B")