def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Ingresa un número entero válido.")
def dibujar_grafico(ancho, altura, espaciado):
    if ancho > 70 or altura > 18 or espaciado >= altura:
        print("Error: Los valores ingresados no cumplen con las restricciones.")
        return
    for i in range(altura):
        if i % espaciado == 0:
            print("*" * (ancho + 4))  # Línea completa
        else:
            print("*" + " " * (ancho + 2) + "*")  # Espacio dentro de la línea
# Solicitar dimensiones del gráfico
ancho = validar_entero("Ancho del gráfico: ")
altura = validar_entero("Altura del gráfico: ")
espaciado = validar_entero("Espaciado: ")

# Dibujar el gráfico
dibujar_grafico(ancho, altura, espaciado)
