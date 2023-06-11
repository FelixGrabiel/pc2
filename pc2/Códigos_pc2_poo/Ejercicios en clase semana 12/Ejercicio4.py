import random
def generar_lista(n):
    lista = list()
    for i in range(n):
        valor = random.randrange(1,6)
        lista.append(valor)
    return lista

while True:
    n = int(input("ingrese cantidad de elementos: "))
    if n > 0:
        break;
listaa = generar_lista(n)
print("VOTOS: ",listaa)
listaconteo=[]
for i in range(5):
    contador = listaa.count(i+1)
    listaconteo.append(contador)
mayor = max(listaconteo)
print("candidatos con mayor votacion")
for i in range(5):
    if listaconteo[i]==mayor:
        print(i+1)