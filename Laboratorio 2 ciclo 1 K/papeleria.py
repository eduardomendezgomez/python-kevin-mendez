"""
Una papeleria vende cuadernos y lapices. Los cuadernos pueden ser de 50 hojas o de 100 hojas.
Los lapices pueden ser de grafito o de colores. El precio de venta es igual al precio de compra
multiplicado por 1.30 que responden al margen de ganancia. La papeleria requiere construir un
programa que le permita registrar y visualizar por lo menos dos articulos de ítem. Todos los 
cuaderno son marca HOJITAS y los lapices son marca RAYAS ya que la papeleria es un distribuidor
exclusivo.
"""
#creamos una clase articulo para los articulos globales con las caracteristicas que tienen en comun
#que son el nombre, la marca, precio de compara y precio de venta 
class Articulo:
    def __init__(self, nombre, marca, precio_compra):
        self.nombre = nombre
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30
    #por medio de esta funcion al final retornada las cadenas, nombre, marca y precio de venta
    def __str__(self):
        return f"Nombre: {self.nombre}, Marca: {self.marca}, Precio de venta: {self.precio_venta}"
    
#con las clase papeleria podremos agregar cuadernos y lapices
class Papeleria:
    #creamos una funcion que tenga una lista de los articulos
    def __init__(self):
        self.articulos = []
    #creamos una funcion para agregar cuadernos y añadirlos al final de  la lista
    def agregar_cuaderno(self, hojas):
        if hojas == 50:
            precio_compra = 7
        elif hojas == 100:
            precio_compra = 17
        cuaderno = Articulo("Cuaderno", "HOJITAS", precio_compra)
        self.articulos.append(cuaderno)
    #creamos una funcion para agregar lapices y añadirlos al final de  la lista
    def agregar_lapiz(self, tipo):
        if tipo == "grafito":
            precio_compra = 5
        elif tipo == "colores":
            precio_compra = 10
        lapiz = Articulo("Lapiz", "RAYAS", precio_compra)
        self.articulos.append(lapiz)
    #creamos una funcion para mostrar los articulos en la lista y creamos un bucle for para que los vaya
    #  mostrando en orden
    def visualizar_articulos(self):
        for articulo in self.articulos:
            print(articulo)
#creamos una instancia de la clase papeleria
papeleria = Papeleria()
#creamos un menu de opciones para que el usuario elija y cuando decida detenerse se terminara la ejecucion del programa
while True:
    print("*********************************************")
    print("Seleccione una de las siguientes opciones: ")
    print("1. Agregar cuaderno")
    print("2. Agregar lapiz")
    print("3. Visualizar articulos")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    print("*********************************************")

    if opcion == "1":
        hojas = int(input("Ingrese el número de hojas del cuaderno (50 o 100): "))
        papeleria.agregar_cuaderno(hojas)
    elif opcion == "2":
        tipo = input("Ingrese el tipo de lapiz (grafito o colores): ")
        papeleria.agregar_lapiz(tipo)
    elif opcion == "3":
        papeleria.visualizar_articulos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")