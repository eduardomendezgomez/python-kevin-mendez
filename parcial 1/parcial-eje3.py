
"""
Ejercicio 3
Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.
 Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa
"""
class Cliente:
    def __init__(self, nombre, apellido,dui,direccion,edad, noches, habitacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad= edad
        self.dui=dui
        self.direccion=direccion
        self.noches = noches
        self.habitacion = habitacion
        self.servicios_extra = []

    def agregar_servicio(self, servicio, costo):
        self.servicios_extra.append((servicio, costo))

    def calcular_total(self, precio_habitacion):
        total = precio_habitacion * self.noches
        for servicio, costo in self.servicios_extra:
            total += costo
        return total

# Habitaciones con la que cuenta el hotel
habitaciones = {
    "basica": 100,
    "premium": 150,
    "Suite": 200
}

servicios_extra = {
    "Piscina": 10,
    "Cancha de golf": 20
}

# aqui se los daria la entrada 
def realizar_reserva():
    print("Bienvenido al hotel de playa Bella Vista!")

    # Mostraria las opciones que cuenta el hotel 
    print("Habitaciones disponibles:")
    for habitacion, precio in habitaciones.items():
        print(f"- {habitacion}: ${precio} por noche")

    # Elegir habitación
    habitacion_elegida = input("Ingrese el tipo de habitación: ").title()
    if habitacion_elegida not in habitaciones:
        print("Habitación no disponible.")
        return

    # Solicitar datos del cliente
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    dui= input("Ingrese su numero de dui: ")
    direccion = input("Ingrese su direccion: ")
    noches = int(input("Ingrese el número de noches: "))

    # Crear objeto cliente
    cliente = Cliente(nombre, apellido,edad,dui,direccion, noches, habitacion_elegida)

    # Ofertar servicios extra
    print("Servicios extra disponibles:")
    for servicio, costo in servicios_extra.items():
        print(f"- {servicio}: ${costo}")

    while True:
        servicio_extra = input("¿Desea agregar algún servicio extra? (s/n): ").lower()
        if servicio_extra == 'n':
            break
        elif servicio_extra == 's':
            servicio = input("Ingrese el servicio: ").title()
            if servicio in servicios_extra:
                cliente.agregar_servicio(servicio, servicios_extra[servicio])
            else:
                print("Servicio no disponible.")
        else:
            print("Opción inválida.")

    # Calcular y mostrar total
    precio_habitacion = habitaciones[habitacion_elegida]
    total = cliente.calcular_total(precio_habitacion)
    print(f"\nFactura para {cliente.nombre} {cliente.apellido} {cliente.edad}{cliente.dui} {cliente.direccion}")
    print(f"Habitación: {cliente.habitacion}")
    print(f"Noches: {cliente.noches}")
    print("Servicios extra:")
    for servicio, costo in cliente.servicios_extra:
        print(f"- {servicio}: ${costo}")
    print(f"Total: ${total}")

realizar_reserva()
        

