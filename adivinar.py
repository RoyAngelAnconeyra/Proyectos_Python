import random

MINIMO = 1

dificultad = input("Elige la dificultad (F,M,D): ")

if dificultad == "F":
    AXIMO = 10
elif dificultad == "M":
    MAXIMO = 50
elif dificultad == "D":
    MAXIMO = 100
elif dificultad not in "DMF":
    print("Erro, no se encontro la dificultad")
    MAXIMO = 10

numero_azar = random.randint(MINIMO, MAXIMO)
intentos = 0

while True:
    intento_usuario = int(input(f"introduce un numero [{MINIMO} - {MAXIMO}]: "))
    intentos += 1
    if intento_usuario > numero_azar:
        print("Te has pasado, el numero es más pequeño que " +str(intento_usuario))
    elif intento_usuario < numero_azar:
        print("Te has quedado corto, el numero es mas grande que " + str(intento_usuario))
    else:
        print("Has acertado")
        break

print("Has acertado, el numeor era  "+ str(numero_azar))
print(f"Has tomado {intentos} intentos")
