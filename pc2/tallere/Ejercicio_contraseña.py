import random as r

class Contraseña:
    def __init__(self, longitud=8):
        self.longitud = longitud
        self.contraseña = self.generarContrasena()

    def generarContrasena(self):
        caracteres = []
        contMayuscula = 0
        contMinuscula = 0
        contNumero = 0

        for _ in range(self.longitud):
            caracterRandom = r.randint(0, 2)

            if caracterRandom == 0:
                caracteres.append(chr(r.randint(65, 90)))
                contMayuscula += 1
            elif caracterRandom == 1:
                caracteres.append(chr(r.randint(97, 122)))
                contMinuscula += 1
            elif caracterRandom == 2:
                caracteres.append(chr(r.randint(48, 57)))
                contNumero += 1

        self.contMayuscula = contMayuscula
        self.contMinuscula = contMinuscula
        self.contNumero = contNumero

        return ''.join(caracteres)

    def esSeguro(self):
        return self.contMayuscula > 2 and self.contMinuscula > 1 and self.contNumero > 5

    def getLongitud(self):
        return self.longitud

    def setLongitud(self, longitud):
        self.longitud = longitud
        self.contraseña = self.generarContrasena()

    def getContraseña(self):
        return self.contraseña

    def mostrarContraseña(self):
        print(f"Contraseña: {self.contraseña}")

# Crear una lista de Contraseñas con tamaño aleatorio entre 6 y 12
tamaño_lista = r.randint(6, 20)
contraseñas = [Contraseña() for _ in range(tamaño_lista)]

# En otra lista de booleanos guardar la información de si las contraseñas son fuertes o no
fortalezas = [contraseña.esSeguro() for contraseña in contraseñas]

# Mostrar en pantalla las contraseñas y su fortaleza
for i in range(len(contraseñas)):
    print(f"Contraseña {i+1} Fuerte: {'V' if fortalezas[i] else 'F'}")
    contraseñas[i].mostrarContraseña()
