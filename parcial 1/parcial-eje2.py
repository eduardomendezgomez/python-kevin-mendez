"""
Una biblioteca ofrece préstamos de libros a través de una tarjeta
impresa que contiene los datos de la persona que realiza el préstamo. El
sistema de préstamos registra la fecha en que se retira el libro y la fecha
límite para su devolución. Realiza un programa que solvente esto de
una manera más eficaz.
Implementar la sección de devolución la cual si la fecha excede la
que devolución se dará una sanción.

Justificacion: se creadon dos clases para mantener los datos de la persona a la que se le realiza el prestamo
como tambien de las fechas en las que lo tendra en uso, y una clase biblioteca para poder agregar y buscar los prestamos
realizados y se uso map para poder facilitar el uso de las fechas y comparaciones.
"""
#creamos una clase de prestamo que tenga todas las caracteristicas y datos del prestamista y el tiempo de uso
class Prestamo:
    def __init__(self, nombre, apellido, fecha_retiro, fecha_devolucion):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_retiro = self.parse_fecha(fecha_retiro)
        self.fecha_devolucion = self.parse_fecha(fecha_devolucion)
        self.fecha_devolucion_real = None
        self.sancion = False
#con esta funcion  damos un funcionamiento para que la fecha que se ingrese se conbierta en formato fecha usando map
    def parse_fecha(self, fecha):
        dia, mes, anio = map(int, fecha.split('-'))
        return (anio, mes, dia)
#la funcion para devolver libro evalua si la fecha de devolución se ha excedido o no y y de ser excedida aplica una sanción.
    def devolver_libro(self, fecha_devolucion_real):
        self.fecha_devolucion_real = self.parse_fecha(fecha_devolucion_real)
        if self.fecha_devolucion_real > self.fecha_devolucion:
            self.sancion = True
            print(f"La devolución del libro ha excedido la fecha límite. Se aplica sanción.")
        else:
            print(f"El libro ha sido devuelto dentro del plazo establecido.")

    def __str__(self):
        return f"Prestamo a {self.nombre} {self.apellido} - Fecha retiro: {self.fecha_retiro[2]}-{self.fecha_retiro[1]}-{self.fecha_retiro[0]} - Fecha devolución: {self.fecha_devolucion[2]}-{self.fecha_devolucion[1]}-{self.fecha_devolucion[0]} - Sanción: {self.sancion}"
#creamos otra clase de la biblioteca donde se mantengan los prestamos de libros como lista, donde tiene funciones para agregar y buscar el prestamo
class Biblioteca:
    def __init__(self):
        self.prestamos = []

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def buscar_prestamo(self, nombre, apellido):
        for prestamo in self.prestamos:
            if prestamo.nombre == nombre and prestamo.apellido == apellido:
                return prestamo
        return None

    def __str__(self):
        return "Biblioteca"

# se crea una instancia de la biblioteca
biblioteca = Biblioteca()

# Agregar préstamos
while True:
    print("Elija una de las siguientes opciones:")
    print("1. Agregar préstamo")
    print("2. Buscar préstamo")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del solicitante: ")
        apellido = input("Ingrese el apellido del solicitante: ")
        fecha_retiro = input("Ingrese la fecha de retiro (dd-mm-aaaa): ")
        fecha_devolucion = input("Ingrese la fecha de devolución (dd-mm-aaaa): ")
        prestamo = Prestamo(nombre, apellido, fecha_retiro, fecha_devolucion)
        biblioteca.agregar_prestamo(prestamo)
        print("Préstamo agregado")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del solicitante: ")
        apellido = input("Ingrese el apellido del solicitante: ")
        prestamo = biblioteca.buscar_prestamo(nombre, apellido)
        if prestamo:
            print(prestamo)
            fecha_devolucion_real = input("Ingrese la fecha de devolución real (dd-mm-aaaa): ")
            prestamo.devolver_libro(fecha_devolucion_real)
        else:
            print("Error: No se encontró el préstamo.")
    elif opcion == "3":
        break
    else:
        print("Error: Opción inválida. Por favor, ingrese una opción válida.")