""""Una veterinaria atiende solamente perros y los registra en una base de datos.
Se requiere un programa que lea la información básica del perro (no mas de 8 caracteristicas)
y se muestre en pantalla. En esta veterinaria todos los animales que llegan entran con un estado
inicial NO ATENDIDO. Por ahora como la veterianaria solo atiende perros, basado en el peso 
(menos de 10kg o mas de 10 kg) los registra como "Perro Grande" o "Perro pequeño"."""

#creamos una clases con las caracteristicas como atributos 
#las caracteristicas serian nombre, edad, peso, color, dueño, estado y el tipo
class Perro: 
    def __init__(self,nombre,edad,peso,raza,color,dueno):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.raza = raza
        self.color = color
        self.dueno = dueno 
        self.estado = "No atendido"
        self.tipo = self.Dtipo()
#creando una funcion que defina conforme al peso si es mayor que 10 es  perro grande, sino, es perro pequeño
    def Dtipo(self):
        if self.peso > 10:
            return "Perro Grande"
        else:
            return "Perro Pequeño"
    #creando una funcion que determine si esta atendido o no  
    def RegistrarPerro(self):
        estado = "Atendido"
        return estado

#con esta función le preguntamos al usuario la informacion requerida 
def IngresarPerro():
    nombre = input("Nombre del perrito: ")
    edad = int(input("Edad del perrito: "))
    peso = float(input("peso del perrito en kg: "))
    raza = input("Raza del perrito: ")
    color = input("Color del perrito: ")
    dueno = input("Nombre del dueño: ")
    print("**************************************************")
    #ingresamos los datos a clase donde esta la informacion de los perros
    nuevoPerro = Perro(nombre,edad,peso,raza,color,dueno)
    return nuevoPerro
#por medio de un funcion imprimimos los datos 
def imprmirDatos(perro):
        print(f"Nombre del perro: {perro.nombre}")
        print(f"Edad del perro: {perro.edad}")
        print(f"Peso del perro: {perro.peso} kg")
        print(f"Raza del perro: {perro.raza}")
        print(f"Color del perro: {perro.color}")
        print(f"Dueño del perro: {perro.dueno}")
        print(f"Tipo de perro: {perro.tipo}")
        print(f"Estado del perro: {perro.estado}")
        print("****************************************************")
#ejecutamos la funcion de imprmir      
perro = IngresarPerro()
imprmirDatos(perro)