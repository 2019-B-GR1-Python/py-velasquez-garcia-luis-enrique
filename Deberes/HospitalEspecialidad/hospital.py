def add_hospital():
    print("\nINGRESE NUEVO HOSPITAL:")
    id_hospital = input("Ingrese el id del nuevo hospital: \n")
    nombre_hospital = input("Ingrese el nombre del nuevo hospital:\n")
    ciudad_hosp= input("Ingrese la ciudad donde se encuentra el hospital:\n")
    num_especialidades = input("Ingrese el numero de especialidades que tiene el nuevo hospital:\n")
    hospital ="\n"+ id_hospital+"\t"+nombre_hospital+"\t"+ciudad_hosp+"\t"+num_especialidades+"\n"
    
    
    try:
        path='./archivo_hospitales.txt'
        archivo_hospitales_abierto = open (path, mode='a')
        for i in hospital:
            archivo_hospitales_abierto.write(i)
        archivo_hospitales_abierto.close()
        print("Hospital ingresado con exito")
    except:
        print("Error al ingresar un nuevo hospital")


def leer_archivo_hopital():
    try:
        archivo_hospitales_abierto = open('./archivo_hospitales.txt')
        contenido = archivo_hospitales_abierto.readlines()
        print("ID HOSPITAL\t NOMBRE\t CIUDAD\t ESPECIALIDADES")
        for line in contenido: # recorre cada linea del string contenido
            print(line)

        archivo_hospitales_abierto.close()
    
    except:
        print("Archivo no encontrado")

# def actualizar_hospital():
   # print("Aun tengo q hacer")

def eleminar_hospital():
    try:
        archivo_hospitales_abierto = open('./archivo_hospitales.txt')
        contenido = archivo_hospitales_abierto.readlines()
        lista_de_hospitales = []
        print("\n"+"ID HOSPITAL\t NOMBRE\t CIUDAD\t ESPECIALIDADES")
        for indice in contenido: # recorre cada linea del string contenido
            print(indice)

        hospital_eliminado = input("Ingrese el id del hospital que se quiere eliminar \n")
        for indice in contenido:
            if not hospital_eliminado in indice:
                lista_de_hospitales.append(indice)

        archivo_hospitales_abierto.close()

        archivo_hospitales_abierto = open('./archivo_hospitales.txt','w')
        archivo_hospitales_abierto.writelines(lista_de_hospitales)
        archivo_hospitales_abierto.close()

    except:
        print("Error, hospital no existente")


