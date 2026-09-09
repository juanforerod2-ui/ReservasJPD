citas = []
siguiente_id = 1

def agendar_cita():
    print("\n---------- AGENDAR CITA ----------")
    global siguiente_id
    cita = {
    "id": siguiente_id,
    "nombre": input("Nombre del paciente: "),
    "doctor": input("Nombre del médico: "),
    "fecha": input("Fecha de la cita (dd/mm/aaaa): "),
    "hora": input("Hora de la cita (hh:mm): ")
    }
    citas.append(cita)
    siguiente_id += 1
    print("Cita agendada con éxito.")


def buscar_disponibilidad():
    print("\n---------- BUSCAR DISPONIBILIDAD ----------")
    fecha = input("Fecha a consultar (dd/mm/aaaa): ")
    hora = input("Hora a consultar (hh:mm): ")
    ocupada = any(cita["fecha"] == fecha and cita["hora"] == hora for cita in citas)
    # any revisa en estos momentos es revisar la tabla de citas
    if ocupada:
        print("la cita esta ocupada")
    else:
        print("la cita esta disponible")


def ver_reservas():
    print("\n---------- MIS RESERVAS ----------")
    if not citas:
        print("No tienes reservas agendadas.")
    for cita in citas:
        print(f"ID: {cita['id']}, Paciente: {cita['nombre']}, Médico: {cita['doctor']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}")

def cancelar_reserva():
    print("\n---------- CANCELAR RESERVA ----------")
    if not id_cancelar:
        print("No hay reservas para cancelar.")
        return
    try: 
        # Uso try por si se llega a crashear o danar el codigo.
        id_cancelar = int(input("Ingrese el ID de la cita a cancelar: "))
    except ValueError:
        # Si me sale un error o falla la conversacion avisamos y salimos sin que se dane el codigo.
        print("ID inválido.")
        return
    # return = devolver
    for cita in citas:
        if cita["id"] == id_cancelar:
            citas.remove(cita)
            print("Cita cancelada con éxito.")
            return
    print("No se encontró una cita con ese ID.")


def mostrar_menu():
    print("\n================================")
    print(" SISTEMA DE RESERVAS - CITAS MEDICAS")
    print("================================")
    print("1. Agendar cita")
    print("2. Buscar una reserva disponible")
    print("3. Ver mis reservas")
    print("4. Cancelar una reserva")
    print("5. Salir")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agendar_cita()
    elif opcion == "2":
        buscar_disponibilidad()
    elif opcion == "3":
        ver_reservas()
    elif opcion == "4":
        cancelar_reserva()
    elif opcion == "5":
        print("Gracias por usar el sistema de reservas. ADIOS")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
        continue

    continuar = input("¿Desea continuar? (si/no): ").lower()
    # lower() convierte todo a minusculas para que no haya problemas con la respuesta del usuario
    if continuar != "si":
        # si el usuario no quiere continuar, se sale del bucle y termina el programa
        print("Gracias por usar el sistema de reservas. ADIOS")
        break