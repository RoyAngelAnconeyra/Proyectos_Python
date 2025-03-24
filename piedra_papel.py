import random

movimientos  = ["piedra", "papel",  "tijera"]

puntos_usuario = 0
puntos_ia = 0

while puntos_usuario < 3 and puntos_ia < 3:

    movimientos_ia = random.choice(movimientos)
    movimiento_usuario = input("Introducir movimiento (Pierda/Papel/Tijera): ")

    if movimiento_usuario.lower() not in movimientos:
        print("El movimiento no está permitido")
        quit()

    print(f"Has sacado {movimiento_usuario}")
    print(f"El ordenador ha sacado {movimientos_ia}")

    if movimiento_usuario.lower == "piedra":
        if movimientos_ia == "piedra":
            print("Empate")
        elif movimientos_ia == "papel":
            print("Has perdido")
            puntos_ia += 1
        elif movimientos_ia == "tijera":
            print("Has ganado")
            puntos_usuario += 1
    elif movimiento_usuario.lower() == "papel":
        if movimientos_ia == "piedra":
            print("Has ganado")
            puntos_usuario += 1
        elif movimientos_ia == "papel":
            print("Empate")
        elif movimientos_ia == "tijera":
            print("Has perdido")
            puntos_ia += 1
    elif movimiento_usuario.lower() == "tijera":
        if movimientos_ia == "piedra":
            print("Has perdido")
            puntos_ia += 1
        elif movimientos_ia == "papel":
            print("Has ganado")
            puntos_usuario += 1
        elif movimientos_ia == "tijera":
            print("Empate")
