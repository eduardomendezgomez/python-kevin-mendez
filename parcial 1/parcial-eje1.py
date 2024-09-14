"""
Un consultorio médico atiende a una serie de pacientes, solo está una
secretaria y en el consultorio hay varios doctores cada paciente llega y
deja sus datos además del motivo de su consulta y posteriormente la
secretaria les asigna la fecha de su consulta.
En el caso que una persona ya tenga una consulta previa en lugar
de tomar datos se le pasará a sala de esperas. Implementa esta
problemática a tu código.

JUSTIFICACIÓN:
Se a presentado esta solución en la cual se pueda agendar a los pacientes y agregarlos a la sala de espera. 
Se realizo con clases y funciones para que sea mas facil el funcionamiento del programa. 
Se crearon dos clases donde se tiene una a los pacientes y otra los datos del consultorio.
"""
class Paciente:
    def __init__(self, nombre, apellido, motivo_consulta):
        self.nombre = nombre
        self.apellido = apellido
        self.motivo_consulta = motivo_consulta
        self.fecha_consulta = None

class Consultorio:
    def __init__(self):
        self.pacientes = []
        self.secretaria = Secretaria()

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        self.secretaria.asignar_fecha_consulta(paciente)

    def enviar_a_sala_de_espera(self, paciente):
        print(f"El paciente {paciente.nombre} {paciente.apellido} ha sido enviado a la sala de espera.")

class Secretaria:
    def __init__(self):
        self.consultas = {}

    def asignar_fecha_consulta(self, paciente):
        if paciente.nombre in self.consultas:
            print(f"El paciente {paciente.nombre} {paciente.apellido} ya tiene una consulta previa.")
            consultorio.enviar_a_sala_de_espera(paciente)
        else:
            fecha_consulta = input("Ingrese la fecha de consulta: ")
            self.consultas[paciente.nombre] = fecha_consulta
            paciente.fecha_consulta = fecha_consulta
            print(f"La fecha de consulta para {paciente.nombre} {paciente.apellido} ha sido asignada para {fecha_consulta}.")

consultorio = Consultorio()

while True:
    print("1. Agregar paciente")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        apellido = input("Ingrese el apellido del paciente: ")
        motivo_consulta = input("Ingrese el motivo de la consulta: ")
        paciente = Paciente(nombre, apellido, motivo_consulta)
        consultorio.agregar_paciente(paciente)
    elif opcion == "2":
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")