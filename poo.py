class Humano:
    def __init__(self, edad):
        self.edad = edad

    def hablar(self, mensaje):
        print(mensaje)

class IngSistemas(Humano):
    def __init__(self):
        print("Hola")

    def programar(self, lenguaje):
        print("Voy a programar en ", lenguaje)

class LicDerecho(Humano):
    def estudiarCaso(self, de):
        print("Debol estudiar el caso de ", de)

class estudioso(IngSistemas, LicDerecho):
    pass


#pedro = Humano(26) # Creando un objeto
#raul = Humano(21)

pedro = IngSistemas()
raul = LicDerecho(27)

print("Soy Pedro y tengo ", pedro.edad)
print("Soy Raul y tengo ", raul.edad)

pedro.hablar("Hola")

raul.hablar("Hola, Pedro!")

