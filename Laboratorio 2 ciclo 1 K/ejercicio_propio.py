"""
Este es un programa que me puede servir o le puede servir a los estudiantes para organizarse. 
Ya que es una herramienta para gestionar tarea y recordatorios. Se podran agregar tareas con una descripcion,
fecha de entrega y prioridad. Se podran marcar tareas como completadas y ver la lista de tareas pendientes y completadas.
"""
#creamos una clase con las caracteristicas de las tareas: descripción, fecha de entrega y prioridad, si esta completa tambien 

class Tarea:
    def __init__(self, descripcion, fecha_entrega, prioridad):
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad
        self.completada = False
    #creamos la funcion que devuelva las cadenas para imprimirlas 
    def __str__(self):
        #si la tarea esta completada o pendiente lo que cambiara sera el estado de la tarea
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - Fecha de entrega: {self.fecha_entrega} - Prioridad: {self.prioridad} - Estado: {estado}\n"
# por medio de esta funcion obtenemos los valores y las opciones del usuario
def main():
    #lista de tarea
    tareas = []
    while True:
        print("**************************************************************")
        print("Seleccion una de las opciones y escriba el numero de la opcion")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas pendientes")
        print("4. Mostrar tareas completadas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("**************************************************")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_entrega = input("Ingrese la fecha de entrega: ")
            prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
            #se agregan las tareas a la lista
            tarea = Tarea(descripcion, fecha_entrega, prioridad)
            tareas.append(tarea)
        elif opcion == "2":
            print("*******************************************")
            #para marcar como completada se escribre el numero de la tarea, si es la primera se escribe "1"
            tarea_id = int(input("Ingrese el ID (1,2,3...) de la tarea a marcar como completada: "))
            for tarea in tareas:
                #se toma como indice la longitud de la lista y se le agrega 1 para obtener valor exacto
                if tarea_id == tareas.index(tarea) + 1:
                    tarea.completada = True
                    print("Tarea marcada como completada")
                    break
            else:
                print("Tarea no encontrada")
        elif opcion == "3":
            #mostramos la lista de tareas pendientes
            print("*********************")
            print("Tareas pendientes:")
            for tarea in tareas:
                if not tarea.completada:
                    print(tarea)
        elif opcion == "4":
            #Mostramos la lista de tareas completadas
            print("Tareas completadas:")
            for tarea in tareas:
                if tarea.completada:
                    print(tarea)
        elif opcion == "5":
            #se termina el programa
            break
        else:
            print("Opción inválida")
#ejecutamos para iniciar la introduccion de campos
main()