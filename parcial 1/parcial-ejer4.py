"""
Una empresa de renta de transporte tiene varios tipos de vehículos a su
disposición cada uno con sus características y coste de renta. La
empresa periódicamente registra los nuevos vehículos que ingresan al
lote para su posterior puesta en renta.
Implementa la funcionalidad de rentar los vehículos disponibles
tomando en cuenta los datos del cliente.
"""
class Auto:
    def __init__(self, marca, modelo, año, tipo, costo_x_dia):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo = tipo
        self.costo_por_dia = costo_x_dia

    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.año}) - Tipo: {self.tipo}"

class Cliente:
    def __init__(self, nombre,apellido, dui, licencia,direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.dui = dui
        self.direccion = direccion
        self.licencia = licencia

class Renta:
    def __init__(self, cliente, vehiculo, dias):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.dias = dias

    def calcular_costo(self):
        return self.vehiculo.costo_x_dia * self.dias

# Lista para almacenar los vehículos disponibles
vehiculos_disponibles = []

# Función para registrar un nuevo vehículo
def registrar_vehiculo():
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    año = int(input("Ingrese el año del vehículo: "))
    tipo = input("Ingrese el tipo de vehículo: ")
    costo_por_dia = float(input("Ingrese el costo por día: "))
    nuevo_vehiculo = Auto(marca, modelo, año, tipo, costo_por_dia)
    vehiculos_disponibles.append(nuevo_vehiculo)
    print("Vehículo registrado exitosamente.")

# aqui donde se rentara el auto
def rentar_vehiculo():
    # Mostrar vehículos disponibles
    print("Vehículos disponibles:")
    for i, vehiculo in enumerate(vehiculos_disponibles, start=1):
        print(f"{i}. {vehiculo}")

    # Elegir vehículo
    indice_vehiculo = int(input("Ingrese el número del vehículo a rentar: ")) - 1
    if indice_vehiculo < 0 or indice_vehiculo >= len(vehiculos_disponibles):
        print("Vehículo no válido.")
        return

    vehiculo_rentado = vehiculos_disponibles.pop(indice_vehiculo)

    # Datos del cliente
    nombre = input("Ingrese su nombre: ")
    dui = input("Ingrese su Dui: ")
    direccion = input("Ingrese su direccion")
    licencia = input("Ingrese su número de licencia: ")
    cliente = Cliente(nombre,dui,direccion, licencia)

    # Duración de la renta
    dias = int(input("Ingrese la cantidad de días de la renta: "))

    # Crearemos lo que seria la renta
    renta = Renta(cliente, vehiculo_rentado, dias)
    print(f"Renta realizada. Costo total: ${renta.calcular_costo()}")

# Ejemplo de uso
registrar_vehiculo()
registrar_vehiculo()
rentar_vehiculo()