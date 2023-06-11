def imprimir_rombo(num):
    for i in range(1, num + 1):
        for j in range(num - i):
            print(" ", end = " ")
        for j in range(1, i + i):
            print(j, end = " ")
        print()

    for i in range(num - 1, 0, -1):
        for j in range(num - i):
            print(" ", end = " ")
        for j in range(1, i + 1):
            print(j, end = " ")
        for j in range(i - 1, 0, -1):
            print(j, end = " ")
        print()

num = int(input("Ingrese un numero: "))
if num<0 or num>11:
    print("Error")
        
imprimir_rombo(num)