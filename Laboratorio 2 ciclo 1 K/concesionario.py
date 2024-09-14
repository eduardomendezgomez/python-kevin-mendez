"""
Un concesionario de autos vende vehículos macionales e importados. 
Todos tienen 4 ruedas y capacidad para 4 pasajeros. Esta información debe
registrarse siempre por raziones de ley. Requiere un programa que le permita
almacenar las 10 principales caracteristicas de los audtos. El precio de venta
de cada auto es igual al precio de compra multiplicado por 1.4 que corresponde a su marge de ganancia.
"""
#creamos la clase auto con las caracteristicas de un auto
class Auto:
    def __init__(self, marca, modelo, anio, precio_compra, nacionalidad, color, transmision, combustible, potencia, tipo_vehiculo):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio_compra = precio_compra
        self.nacionalidad = nacionalidad
        self.color = color
        self.transmision = transmision
        self.combustible = combustible
        self.potencia = potencia
        self.tipo_vehiculo = tipo_vehiculo
        self.precio_venta = precio_compra * 1.4
    #creamos una funcion para que pueda devolver las cadenas y pueda presentarlas en la consola o imprimirlos
    def __str__(self):
        return f"Marca: {self.marca} \n" \
        f"Modelo: {self.modelo}\n" \
        f"Año: {self.anio}\n"\
        f"Precio de Compra: {self.precio_compra}\n" \
        f"Nacionalidad: {self.nacionalidad}\n"\
        f"Color: {self.color}\n"\
        f"Transmision: {self.transmision}\n"\
        f"Combustible: {self.combustible}\n"\
        f"Potencia: {self.potencia}\n"\
        f"Tipo de Vehiculo: {self.tipo_vehiculo}\n"\
        f"Precio de Venta: {self.precio_venta:.2f}"
#por medio de la funcion main vamos a obtener los datos que el usuario nos indique
def main():
    print("*******************************")
    print("Ingrese los datos del auto:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio = int(input("Año: "))
    precio_compra = float(input("Precio de Compra: "))
    nacionalidad = input("Nacionalidad: ")
    color = input("Color: ")
    transmision = input("Transmision: ")
    combustible = input("Combustible: ")
    potencia = int(input("Potencia(HP): "))
    tipo_vehiculo = input("Tipo de Vehiculo")
#creamos una instancia de la clase auto para introducir los datos que obtuvimos del usuario y los mostramos
    auto = Auto(marca, modelo, anio, precio_compra, nacionalidad, color, transmision, combustible, potencia, tipo_vehiculo)
    print("\nDatos del auto:")
    print(auto)
#llamamos a la funcion para que se ejecute y obtener los datos del usuario
main()