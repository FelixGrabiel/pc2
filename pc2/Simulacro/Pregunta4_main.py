import random
from Pregunta4 import CDato

num = int(input("Ingrese la cantidad de encuestas realizadas: "))
if num <= 0 or num > 45:
    print("Error, la cantida deber mayor que 0 y menor que 45")
    exit()
provincias = ["Lima", "Arequipa", "Piura"]
generos = ["Masculino", "Femenino"]
satisfacciones = ["Satisfecho", "Insatisfecho"]

encuestas = []
for _ in range(num):
    provincia = random.sample(provincias, 1)[0]
    genero = random.sample(generos, 1)[0]
    satisfaccion = random.sample(satisfacciones, 1)[0]
    edad = random.randint(18, 90)

    encuesta = CDato(provincia, genero, satisfaccion, edad)
    encuestas.append(encuesta)

print("Datos de cada encuestado:")
for i, encuesta in enumerate(encuestas, start=1):
    print(f"Encuestado {i}:")
    encuesta.consultardatos()
    print("--------------------")
print("===REPORTE===")
edades = [encuesta.get_edad() for encuesta in encuestas]
max_edad = max(edades)
min_edad = min(edades)
print("Máxima edad:", max_edad)
print("Mínima edad:", min_edad)

total_encuestas = len(encuestas)
satisfechos = sum(encuesta.get_satisfaccion() == "Satisfecho" for encuesta in encuestas)
insatisfechos = total_encuestas - satisfechos

porcentaje_satisfechos = (satisfechos / total_encuestas) * 100
porcentaje_insatisfechos = (insatisfechos / total_encuestas) * 100

print("Porcentaje de personas satisfechas:", porcentaje_satisfechos)
print("Porcentaje de personas insatisfechas:", porcentaje_insatisfechos)

promedios_edad = {}
for provincia in provincias:
    edades_provincia = [encuesta.get_edad() for encuesta in encuestas if encuesta.get_provincia() == provincia]

    if len(edades_provincia) > 0:  
        promedio_edad_provincia = sum(edades_provincia) / len(edades_provincia)
    else:
        promedio_edad_provincia = 0  

    promedios_edad[provincia] = promedio_edad_provincia

print("Promedio de edad por provincia:")
for provincia, promedio_edad in promedios_edad.items():
    print(f"{provincia}: {promedio_edad}")
