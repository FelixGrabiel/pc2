class Hora:
    __hora = 0
    __minuto = 0
    __segundo = 0

    def __init__(self, hora, minuto, segundo):
        self.setHora(hora, minuto, segundo)

    def setHora(self, hora, minuto, segundo):
        self.__hora = hora if 0 <= hora <= 23 else 0
        self.__minuto = minuto if 0 <= minuto <= 59 else 0
        self.__segundo = segundo if 0 <= segundo <= 59 else 0

    def getHora(self):
        return [self.__hora, self.__minuto, self.__segundo]

    def imprimirHora(self):
        print(f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}")

    def incrementarSegundo(self):
        segundosTotales = self.transformarASegundos() + 1
        self.__hora = segundosTotales // 3600
        segundosTotales %= 3600
        self.__minuto = segundosTotales // 60
        self.__segundo = segundosTotales % 60

    def cuantoFaltaParaFinalDia(self):
        segundosTotales = self.transformarASegundos()
        segundosFaltantes = 24 * 3600 - segundosTotales
        hora = segundosFaltantes // 3600
        segundosFaltantes %= 3600
        minuto = segundosFaltantes // 60
        segundo = segundosFaltantes % 60
        print(f"Para el final del día faltan: {hora} horas:{minuto} minuto:{segundo} segundo")

    def transformarASegundos(self):
        return self.__hora * 3600 + self.__minuto * 60 + self.__segundo

def ingresar(lista):
    while True:
        hora = int(input("Ingrese hora (o -1 para salir): "))
        if hora == -1:
            break

        minuto = int(input("Ingrese minuto: "))
        segundo = int(input("Ingrese segundo: "))

        lista.append(Hora(hora, minuto, segundo))


def incrementar(lista):
    for hora in lista:
        hora.incrementarSegundo()
        hora.imprimirHora()


def diferenciaHoraria(lista):
    listaSegundos = [hora.transformarASegundos() for hora in lista]
    mayorS = max(listaSegundos)
    menorS = min(listaSegundos)
    segundosDiferencia = mayorS - menorS
    hora = segundosDiferencia // 3600
    segundosDiferencia %= 3600
    minuto = segundosDiferencia // 60
    segundo = segundosDiferencia % 60
    print(f"De la mayor hora a la menor hora hay {hora}:{minuto}:{segundo} de diferencia")


horas = []
ingresar(horas)
incrementar(horas)
diferenciaHoraria(horas)
for hora in horas:
    hora.cuantoFaltaParaFinalDia()
