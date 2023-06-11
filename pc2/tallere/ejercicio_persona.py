import random as r

class CPersona:
    # Atributos privados inicializados por defecto
    def __init__(self, nombre='', edad=0, sexo='H', peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.generaDNI()

    # Métodos get
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getSexo(self):
        return self.__sexo

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura

    def getDNI(self):
        return self.__dni

    # Métodos set
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad

    def setSexo(self, sexo):
        self.__sexo = sexo

    def setPeso(self, peso):
        self.__peso = peso

    def setAltura(self, altura):
        self.__altura = altura

    def setDNI(self, dni):
        self.__dni = dni

    # Método para hallar el IMC
    def calcularIMC(self):
        pesoIdeal = self.__peso / (self.__altura ** 2)

        if pesoIdeal < 20:
            return -1
        elif pesoIdeal >= 20 and pesoIdeal <= 25:
            return 0
        else:
            return 1

    # Método para saber si es mayor de edad
    def esMayorDeEdad(self):
        return self.__edad >= 18

    # Método para generar DNI aleatorio
    def generaDNI(self):
        return r.randint(10000000, 99999999)

    # Método para mostrar datos
    def mostrarDatos(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("Sexo:", self.__sexo)
        print("DNI:", self.__dni)
        print("Peso:", self.__peso)
        print("Altura:", self.__altura)

# Ingreso de datos
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (H:Hombre; M:Mujer): ")
altura = float(input("Ingrese la altura: "))
peso = float(input("Ingrese el peso: "))

# Creamos objeto de la clase Persona
objPersona = CPersona(nombre, edad, sexo, peso, altura)

# Mostramos datos
objPersona.mostrarDatos()

# Comprobamos el peso ideal
if objPersona.calcularIMC() == -1:
    print("Peso ideal")
elif objPersona.calcularIMC() == 0:
    print("Debajo de su peso ideal")
elif objPersona.calcularIMC() == 1:
    print("Sobrepeso")

# Comprobamos si es mayor de edad
if objPersona.esMayorDeEdad():
    print("Es mayor de edad")
else:
    print("Es menor de edad")
