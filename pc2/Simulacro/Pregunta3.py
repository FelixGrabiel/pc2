import random

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [random.randint(1, 3) for j in range(columnas)]
        matriz.append(fila)
    return matriz

def contar_cultivos(matriz):
    frecuencias = {1: 0, 2: 0, 3: 0}
    for fila in matriz:
        for cultivo in fila:
            frecuencias[cultivo] += 1
    return frecuencias

def determinar_frecuencia(frecuencias):
    mayor = max(frecuencias, key=frecuencias.get)
    menor = min(frecuencias, key=frecuencias.get)
    return mayor, menor

def buscar_guarida_topo(matriz):
    guaridas = []
    for i in range(len(matriz)-2):
        for j in range(len(matriz[i])-2):
            if matriz[i][j] == 1 and matriz[i][j+1] == 3 and matriz[i][j+2] == 2 and matriz[i+1][j+1] == 2:
                guaridas.append((i, j+1))
    return guaridas

filas = 10
columnas = 15

matriz = generar_matriz(filas, columnas)
print("Matriz:")
for fila in matriz:
    print(fila)

frecuencias = contar_cultivos(matriz)
mayor, menor = determinar_frecuencia(frecuencias)
print("\nCultivo con mayor frecuencia:", mayor)
print("Cultivo con menor frecuencia:", menor)

guaridas = buscar_guarida_topo(matriz)
if guaridas:
    print("\nPuntos de posibles guaridas de topos:")
    for guarida in guaridas:
        print(guarida)
else:
    print("\nNo se encontraron puntos de posibles guaridas de topos.")
