class CPersona:
    __nombre = ""
    __edad = 0
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad

class CLista:
    __lista = []
    
    def agregar(self, elemento):
        self.__lista.append(elemento)
    
    def get_lista(self):
        return self.__lista
    
    def promedio_edad(self):
        suma = 0
        for x in self.__lista:
            suma = suma + x.get_edad()
        return suma / len(self.__lista)
    
    def mayor_edad(self):
        mayor = -1
        nombre = ""
        for x in self.__lista:
            if x.get_edad() > mayor:
                mayor = x.get_edad()
                nombre = x.get_nombre()
        return nombre
    
    def listar_datos(self):
        for x in self.__lista:
            print(x.get_nombre(), "\t", x.get_edad())

lista = CLista()
nombre = "a"
while nombre != "":
    nombre = input("Ingrese nombre: ")
    if nombre != "":
        edad = int(input("Ingrese la edad: "))
        if edad > 1:
            objeto = CPersona(nombre, edad)
            lista.agregar(objeto)
        else:
            break

lista.listar_datos()
print("Promedio =", lista.promedio_edad())
print("Nombre de persona con mayor edad =", lista.mayor_edad())
