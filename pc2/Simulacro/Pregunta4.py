class CDato:
    def __init__(self, provincia, genero, satisfaccion, edad):
        self.__provincia = provincia
        self.__genero = genero
        self.__satisfaccion = satisfaccion
        self.__edad = edad

    def get_provincia(self):
        return self.__provincia

    def set_provincia(self, provincia):
        self.__provincia = provincia

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_satisfaccion(self):
        return self.__satisfaccion

    def set_satisfaccion(self, satisfaccion):
        self.__satisfaccion = satisfaccion

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def consultardatos(self):
        print("Provincia:", self.__provincia)
        print("Género:", self.__genero)
        print("Nivel de Satisfacción:", self.__satisfaccion)
        print("Edad:", self.__edad)
