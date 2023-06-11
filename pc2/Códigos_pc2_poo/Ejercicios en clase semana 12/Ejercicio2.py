class Persona:
    __nombre = " "
    __edad = 0
    
    def __init__(self, nomb, edad):
        self.__nombre = nomb
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad

lista = []
nombre = "a"

while nombre != "":
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    if edad>1:
        objeto = Persona(nombre, edad)
        lista.append(objeto)
    else:
        break


print("Nombre\tEdad")
for x in lista:
    print(x.get_nombre(), "\t", x.get_edad())
