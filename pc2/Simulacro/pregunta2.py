import random

def imprimir_secuencias_ascendentes(lista):
    secuencias = []
    secuencia_actual = []

    for num in lista:
        if not secuencia_actual or num >= secuencia_actual[-1]:
            secuencia_actual.append(num)
        else:
            secuencias.append(secuencia_actual)
            secuencia_actual = [num]
    
    secuencias.append(secuencia_actual)

    for secuencia in secuencias:
        print(' '.join(str(num) for num in secuencia))


numero_elementos = int(input("Ingrese el número de elementos de la lista (no mayor a 50): "))

if numero_elementos > 50 :
    print("El número de elementos no puede ser mayor a 50.")
else:
    lista = [random.randint(1, 100) for _ in range(numero_elementos)]
    print("Lista generada:", lista)
    print("Secuencias ascendentes encontradas:")
    imprimir_secuencias_ascendentes(lista)
