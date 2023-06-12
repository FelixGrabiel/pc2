def ingresar_notas():
    notas = []
    for i in range(8):
        nota = float(input("Ingrese la nota del alumno: "))
        notas.append(nota)
    return notas

def calcular_promedio(notas):
    notas.sort(reverse=True)
    mejores_notas = notas[:6]
    promedio = sum(mejores_notas) / len(mejores_notas)
    return promedio

notas_alumno = ingresar_notas()
promedio = calcular_promedio(notas_alumno)
print("El promedio de las 6 mejores notas es:", promedio)
