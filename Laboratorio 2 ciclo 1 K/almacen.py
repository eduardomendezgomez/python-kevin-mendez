"""
Un alamcen vende dispositivos electronicos (celulares, tablets y portatiles) 
Todos PHR que es una nueva marca que esta entrando en el mercado. Se requiere 
almacenar sus 6 principales gcaracterísticas. Todos son productos importados y
 su precio de venta es igual al precio de compra por 1.7 que corresponde a su margen de ganancia.
"""
#Primero creamos la clase dispositivo con las caracteristicas que tienen en comun los dispositivos
class Dispositivo:
    def __init__(self, tipo, modelo, caracteristicas, precio_compra):
        self.tipo = tipo
        self.modelo = modelo
        self.caracteristicas = caracteristicas
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    #calculamos el precio de la venta multiplicando el precio de compra por 1.7
    def calcular_precio_venta(self):
        return self.precio_compra * 1.7
    #creamos una funcion que retorne las cadenas en la cual se detallaran en la consola el tipo de dispositivo
    # las caracteristicas del dispostivo, el precio de compra y el precio de venta
    def __str__(self):
        #col el ".2f" no referimos a que nos muestre unicamente dos digitos despues del punto
        return f"Dispositivo Electrónico {self.modelo} ({self.tipo})\n" \
               f"Características: {', '.join(self.caracteristicas)}\n" \
               f"Precio de Compra: ${self.precio_compra:.2f}\n" \
               f"Precio de Venta: ${self.precio_venta:.2f}"
#por medio de esta funcion obtenemos las caracteristicas del dispositivo y las guardamos en una lista al final
def obtener_caracteristicas():
    caracteristicas = []
    while True:
        caracteristica = input("Introduzca una característica (o 'fin' para terminar): ")
        if caracteristica.lower() == 'fin':
            break
        caracteristicas.append(caracteristica)
    return caracteristicas
#con esta función obtenemos los campos de entrada del usuario 
def main():
    print("*************************************************")
    print("Introduzca los datos del dispositivo electrónico:")
    tipo = input("Tipo (Celular, Tablet, Portátil): ")
    modelo = input("Modelo: ")
    caracteristicas = obtener_caracteristicas()
    precio_compra = float(input("Precio de Compra: $"))
# enviamos los datos obtenidos a la clase Dispositivo 
    dispositivo = Dispositivo(tipo, modelo, caracteristicas, precio_compra)
    print("**************************************")
    print("\nDatos del dispositivo electrónico:")
    print(dispositivo)
    print("**************************************")
#ejecutamos la función main para introducier los datos 
main()