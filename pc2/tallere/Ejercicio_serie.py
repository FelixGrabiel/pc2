def generar_serie_fibonacci(cantidad):
    serie = []
    a, b = 1, 1
    for _ in range(cantidad):
        serie.append(a)
        a, b = b, a + b
    return serie

cantidad = int(input("Ingrese la cantidad de números de la serie: "))
serie_fibonacci = generar_serie_fibonacci(cantidad)
print(serie_fibonacci)
