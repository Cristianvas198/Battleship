# 🛳️ Battleship - Juego de Batalla Naval 🛳️

¡Bienvenido/a a **Battleship**, un emocionante juego de estrategia para hundir la flota enemiga antes de que te hundan a ti! Este proyecto ha sido creado en Python y simula una batalla naval épica entre el jugador y la máquina. 🚢

---

## 🎮 Cómo Jugar

### Objetivo
Tu misión es hundir todos los barcos enemigos antes de que la máquina hunda los tuyos. Usa tu ingenio y precisión para disparar y ganar la batalla.

### Reglas del Juego
1. Ambos jugadores (tú y la máquina) tienen una flota oculta en un tablero de 10x10.
2. Cada jugador dispara por turnos. 
3. Los barcos se colocan de forma estratégica en el tablero:
   - **1 Portaviones** (Eslora: 4 casillas).
   - **2 Yates** (Eslora: 3 casillas cada uno).
   - **3 Botes** (Eslora: 2 casillas cada uno).
4. ¡El primero en hundir todos los barcos del oponente gana! Un barco se considera hundido cuando todas sus casillas son impactadas.

---

## ⚙️ Características

- **Colocación Estratégica**: Tú decides la dirección de tus barcos (Norte, Sur, Este, Oeste). La máquina también posiciona sus barcos de manera inteligente.
- **Disparos por Turnos**: Dispara en las coordenadas deseadas y descubre si acertaste o fallaste.
- **Tablero Oculto**: Los barcos del enemigo están ocultos para ti, pero puedes ver los impactos de tus disparos.
- **Mensajes Informativos**: Recibes actualizaciones constantes, como si acertaste, fallaste, o disparaste en una posición repetida.

---

## 📋 Instrucciones Detalladas

### 1. Inicio
- Ejecuta el programa en tu terminal.
- Responde `S` o `N` cuando se te pregunte si deseas comenzar la partida.

### 2. Colocación de Barcos
- Para cada barco (Portaviones, Yate, Bote), elige la dirección:
  - **Norte**: El barco se extiende hacia arriba.
  - **Sur**: El barco se extiende hacia abajo.
  - **Este**: El barco se extiende hacia la derecha.
  - **Oeste**: El barco se extiende hacia la izquierda.
- El programa genera automáticamente posiciones válidas para cada barco.

### 3. Turnos de Disparo
- En tu turno, ingresa las coordenadas de fila y columna donde quieres disparar.
- Evita disparar en una posición donde ya disparaste. Si lo haces, recibirás un mensaje: `"Ya has disparado aquí. Intenta nuevamente."`
- El programa verificará si el disparo es válido:
  - **Impacto en un barco enemigo**: Se marcará con `X`.
  - **Disparo al agua**: Se marcará con `A`.
  - **Ya disparado**: Se te pedirá ingresar nuevas coordenadas.

### 4. Ganar o Perder
- **Ganas** si hundes todos los barcos enemigos.
- **Pierdes** si la máquina hunde todos tus barcos.

---

## 🔧 Requisitos Técnicos

- **Python 3.6+**
- Biblioteca `numpy`: Para manejar los tableros como matrices.

