class CTriangulo:
    # atributos privados
    __base = 0
    __altura = 0

    # constructor
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    # metodos de acceso
    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def set_base(self, base):
        self.__base = base

    def set_altura(self, altura):
        self.__altura = altura

    # otros metodos
    def area(self):
        return self.__base * self.__altura / 2

    def perimetro(self):
        hipotenusa = (self.__base**2 + self.__altura**2)**0.5
        return self.__base + self.__altura + hipotenusa

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
objeto = CTriangulo(base, altura)

print("Area = ", objeto.area())
print("Perimetro = ", objeto.perimetro())
