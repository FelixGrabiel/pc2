class CuentaCorriente:
    def __init__(self, dni="", nombre="", apellidos="", distrito="", telefono="", saldo=0.0):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__distrito = distrito
        self.__telefono = telefono
        self.__saldo = saldo
    
    def set_dni(self, dni):
        self.__dni = dni
    
    def get_dni(self):
        return self.__dni
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
    
    def get_apellidos(self):
        return self.__apellidos
    
    def set_distrito(self, distrito):
        self.__distrito = distrito
    
    def get_distrito(self):
        return self.__distrito
    
    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def get_telefono(self):
        return self.__telefono
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def get_saldo(self):
        return self.__saldo
    
    def retirarDinero(self, cantidad):
        self.__saldo -= cantidad
    
    def ingresarDinero(self, cantidad):
        self.__saldo += cantidad
    
    def consultarCuenta(self):
        print("Datos de la cuenta:")
        print("DNI:", self.__dni)
        print("Nombre:", self.__nombre)
        print("Apellidos:", self.__apellidos)
        print("Distrito:", self.__distrito)
        print("Teléfono:", self.__telefono)
        print("Saldo:", self.__saldo)
    
    def saldoNegativo(self):
        return self.__saldo < 0
# Lista para almacenar las cuentas corrientes
cuentas = []

# Ingresar los datos de las cuentas
while True:
    dni = input("Ingrese el DNI (dejar vacío para terminar): ")
    if dni == "":
        break
    
    # Verificar la longitud del DNI
    if len(dni) != 8:
        print("El DNI debe tener una longitud de 8 caracteres.")
        continue
    
    nombre = input("Ingrese el nombre: ")
    apellidos = input("Ingrese los apellidos: ")
    distrito = input("Ingrese el distrito: ")
    telefono = input("Ingrese el teléfono: ")
    saldo = float(input("Ingrese el saldo: "))
    
    cuenta = CuentaCorriente(dni, nombre, apellidos, distrito, telefono, saldo)
    cuentas.append(cuenta)

# Realizar una transferencia de dinero
dni_retira = input("Ingrese el DNI de la persona que retira dinero: ")
dni_deposita = input("Ingrese el DNI de la persona a quien se le deposita el dinero: ")
cantidad = float(input("Ingrese la cantidad a transferir: "))

cuenta_retira = None
cuenta_deposita = None

for cuenta in cuentas:
    if cuenta.get_dni() == dni_retira:
        cuenta_retira = cuenta
    elif cuenta.get_dni() == dni_deposita:
        cuenta_deposita = cuenta

if cuenta_retira is None:
    print("No se encontró la cuenta con el DNI especificado para retirar dinero.")
elif cuenta_deposita is None:
    print("No se encontró la cuenta con el DNI especificado para depositar dinero.")
else:
    cuenta_retira.retirarDinero(cantidad)
    cuenta_deposita.ingresarDinero(cantidad)
    print("Transferencia realizada.")

# Calcular y mostrar el saldo promedio de personas en un distrito
distrito_buscar = input("Ingrese el distrito para calcular el saldo promedio: ")
personas_distrito = [cuenta for cuenta in cuentas if cuenta.get_distrito() == distrito_buscar]

if len(personas_distrito) > 0:
    saldo_total = sum(cuenta.get_saldo() for cuenta in personas_distrito)
    saldo_promedio = saldo_total / len(personas_distrito)
    print("El saldo promedio de las personas en el distrito", distrito_buscar, "es:", saldo_promedio)
else:
    print("No hay personas registradas en el distrito especificado.")

# Mostrar los datos de las personas cuyo apellido empieza con una determinada letra
letra_buscar = input("Ingrese la letra para buscar personas por apellido: ")

personas_letra = [cuenta for cuenta in cuentas if cuenta.get_apellidos()[0] == letra_buscar.upper()]

if len(personas_letra) > 0:
    print("Personas cuyo apellido empieza con la letra", letra_buscar + ":")
    for cuenta in personas_letra:
        cuenta.consultarCuenta()
        print()
else:
    print("No hay personas cuyo apellido empiece con la letra especificada.")

# Encontrar la(s) persona(s) con el mayor saldo
mayor_saldo = max(cuenta.get_saldo() for cuenta in cuentas)
personas_mayor_saldo = [cuenta for cuenta in cuentas if cuenta.get_saldo() == mayor_saldo]

print("Persona(s) con mayor saldo:")
for cuenta in personas_mayor_saldo:
    cuenta.consultarCuenta()
    print()
