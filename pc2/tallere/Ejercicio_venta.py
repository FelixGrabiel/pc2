def calcular_subtotal(ventas):
    subtotal = 0
    for producto, cantidad, precio in ventas:
        subtotal += cantidad * precio
    return subtotal

def calcular_impuesto(subtotal):
    impuesto = subtotal * 0.18
    return impuesto

def mostrar_ventas(ventas):
    subtotal = calcular_subtotal(ventas)
    impuesto = calcular_impuesto(subtotal)
    total = subtotal + impuesto

    print("Ventas realizadas:")
    for producto, cantidad, precio in ventas:
        print("Producto: ",producto)
        print("Cantidad: ",cantidad)
        print("Precio Unitario: S/",precio)
        print("Subtotal: S/",cantidad*precio)
        print("--------------------------")

    print(f"Subtotal: S/{subtotal}")
    print(f"Impuesto (18%): S/{impuesto}")
    print(f"Total: S/{total}")

def main():
    diccionario_A = {}
    ventas = []

    while True:
        print("===== MENU =====")
        print("1) Ingreso de Producto")
        print("2) Ingreso de Venta de Producto")
        print("3) Listado de Productos Vendidos con Total")
        print("4) Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ")
            stock = int(input("Ingrese la cantidad de stock: "))
            precio_unitario = float(input("Ingrese el precio unitario: "))

            diccionario_A[producto] = {'stock': stock, 'precio_unitario': precio_unitario}
            print("Producto ingresado exitosamente.")

        elif opcion == "2":
            producto = input("Ingrese el nombre del producto: ")
            if producto not in diccionario_A:
                print("El producto no existe en el inventario.")
                continue

            stock = diccionario_A[producto]['stock']
            if stock == 0:
                print("No hay stock disponible para ese producto.")
                continue

            cantidad = int(input("Ingrese la cantidad a vender: "))
            if cantidad > stock:
                print("No hay suficiente stock para esa venta.")
                continue

            precio_unitario = diccionario_A[producto]['precio_unitario']
            precio_venta = cantidad * precio_unitario

            ventas.append((producto, cantidad, precio_unitario))
            diccionario_A[producto]['stock'] -= cantidad

            print(f"Venta de {cantidad} unidades de {producto} realizada exitosamente.")
            print(f"Precio de venta: ${precio_venta}")

        elif opcion == "3":
            mostrar_ventas(ventas)

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
