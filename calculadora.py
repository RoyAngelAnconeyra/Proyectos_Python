
numero1 = int(input("Introduce numero 1: "))
numero2 = int(input("Introduce numero 2: "))

operaciones_posibles = ["+", "-", "*", "/"]

operaciones = input("Introduce una operacion [+ - * /]: ")

while operacion not in operaciones_posibles:
    operacion = input("Introduce una operacion [+ - * /]: ")

try:
    resultado = eval(f"{numero1} {operacion} {numero2}")
except ZeroDivisionError:
    print("Error al dividir por cero")

print(f"{numero1} {operacion} {numero2} = {resultado}")



