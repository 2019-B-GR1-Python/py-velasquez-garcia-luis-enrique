import hospital

def opciones_hospital(opcion):

    try:
        return {
            0: None,
            1:hospital.add_hospital,
            2:hospital.leer_archivo_hopital,
            3: hospital.eleminar_hospital,

        }[opcion]
    except KeyError:
        print("Opcion invalida")

def menu_hospital(opcion):
    print("\n Editar Hospitales")
    print("1.Ingresar nuevo Hospital.")
    print("2. Mostar hospitales.")
    print("3. Eliminar Hospital.")

    opcion_seleccionada = input("Escoja una opcion:")
    if(opcion_seleccionada.isnumeric()):
        opcion= int(opcion_seleccionada)
    try:
        opciones_hospital(opcion)()
    except TypeError:
        print("seleccion invalida")

def opciones_menu_principal(opcion):
    try:
        return {
            0:None,
            1:menu_hospital,
        }[opcion]
    except KeyError:
        print("Error, opcion invalida")

def menu_principal(opcion):
    print("Hospital-Especialidad")
    print("1. Hospital")
    print("2. Especialidades")

    opcion_seleccionada = input("Escoja una opcion:")
    if(opcion_seleccionada.isnumeric()):
        opcion= int(opcion_seleccionada)

    if(opcion == 1):
        menu_hospital("Hospital")
    #elif (opcion==2):
        #opc_especialidad("Especialidades")
    else:
        print("\n")

    try:
        opciones_menu_principal(opcion)()
    except TypeError:
        print("Error")

menu_principal(-1)
