import random
import time
import numpy as np
from utils import *

# ----------------------------------------------------------- Bienvenida ---------------------------------------------------------------------------

# Bienvenida al jugador
time.sleep(2)
print("        |    |    |")
print("     )__)  )__)  )__)")
print("    )____)____)_____)")
print("    |   BATTLESHIP   |")
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print()
time.sleep(5)
print("🛳️ Bienvenid@ a Battleship 🛳️")
time.sleep(2)
print("¡Prepárate para una batalla naval épica contra la máquina!")
time.sleep(2)

# ----------------------------------------------------------- Instrucciones --------------------------------------------------------------------

# Explicar las instrucciones del juego
print("Tu misión es hundir todos los barcos del enemigo antes de que él hunda los tuyos.\n\n"
      "Ambos jugadores (tú y la máquina) tendrán una flota oculta en el tablero.\n"
      "¡Dispara con precisión y usa tu estrategia para ganar!")
time.sleep(2)

# ----------------------------------------------------------- Desea-jugar? ---------------------------------------------------------------------

comenzar = input("¿Desea comenzar la partida? S/N: ").strip().lower()
if comenzar == "n":  # Si responde NO, mostrar un mensaje de despedida y salir del programa.
    print("Regresa pronto. ¡Fin del juego!")
    exit()
elif comenzar == "s":  # Si responde SI, inicia el juego.
    print("\nComienza el juego 🛳️")
    time.sleep(3)

# ----------------------------------------------------------- Comienza-el-juego --------------------------------------------------------------------

tablero_jugador = crear_tablero()
tablero_maquina = crear_tablero()


for n, eslora in enumerate([4, 3, 2], start=1):  # Portaviones, Yate, Bote
    direccion = input(f"Ingrese dirección del barco {n} (Norte, Sur, Este, Oeste): ").strip().lower() #El jugador ingresa la orientacion de barco
    barco = crear_barco_direccion(eslora, tablero_jugador, direccion)
    colocar_barco(barco, tablero_jugador)

for eslora in [4, 3, 2]:  #para generar los barcos de la maquina
    while True:
        direccion_maquina = random.choice(["norte", "sur", "este", "oeste"]) #genera la direccion del barco de forma aleatoria
        barco_maquina = crear_barco_direccion(eslora, tablero_maquina, direccion_maquina)
        if barco_maquina: 
            colocar_barco(barco_maquina, tablero_maquina)
            break

while True:
    print("\nTu tablero:")  #muestra el tablero del jugador
    for fila in tablero_jugador:
        print(" ".join(fila))
    
    time.sleep(2)
    tablero_maquina_base(tablero_maquina)  #muestra el tablero de la máquina
    time.sleep(2)

    print("\nTu turno de disparar:")  # Jugador dispara
    while True:
        fila_disparo = int(input("Ingresa la fila del disparo (0-9): "))
        columna_disparo = int(input("Ingresa la columna del disparo (0-9): "))
        
        if not (0 <= fila_disparo <= 9 and 0 <= columna_disparo <= 9): 
            print("Coordenadas no validas")
            continue  
        
        if tablero_maquina[fila_disparo, columna_disparo] in ["X", "A"]:
            print("Ya has disparado aquí, intentalo nuevamente.")
            continue 

        disparar((fila_disparo, columna_disparo), tablero_maquina) #Si las coordenadas son validas "imprime" el disparo
        time.sleep(2)

        if ganar(tablero_maquina): #comprueba si el jugador gana
            print("Ganaste!!")
            print("              |    |    |")
            print("             )_)  )_)  )_)")
            print("            )___))___))___)")
            print("           )____)____)_____)\_")
            print("         _____|____|____|____\\__")
            print("---------\\                   /---------")
            print("  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^")
            print("    ^^^^      ¡VICTORIA!     ^^^")
            print("         Todos los barcos enemigos")
            print("          han sido hundidos.⚓") 
            exit()  #finaliza el juego si el jugador gana

        break  #le pasa el turno a la maquina

    print("\nTurno de la máquina...")
    while True:
        fila_maquina = random.randint(0, 9) #se generan posiciones random para el disparo por parte de la maquina
        columna_maquina = random.randint(0, 9)
        if tablero_jugador[fila_maquina, columna_maquina] not in ["X", "A"]:
            break
    disparar((fila_maquina, columna_maquina), tablero_jugador) #Si las coordenadas son validas "imprime" el disparo

    if ganar(tablero_jugador):#comprueba si la maquina gana
        print("Perdiste. La máquina hundió todos tus barcos.")
        print()
        print("     🦈    🦈    🦈")
        print("    🦈  ¡Banquete!  🦈")
        print("      __/___     ")
        print("  _____/______|   ")
        print("  \\__________/")
        print()
        print(" Los tiburones disfrutaron de tu derrota. 💀")
        print(" GAME OVER")

        break