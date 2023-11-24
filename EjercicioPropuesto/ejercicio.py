#Se define una clase llamada equipo que representa un equipo de computo
class EquipoComputo:
    def _init_(self, idEquipo, cargador, mouse, ambiente):
        #se inicializa los atributos del equipo
        self.ID = idEquipo
        self.Cargador = cargador
        self.Mouse = mouse
        self.Ambiente = ambiente
        self.Novedades = []#lista para almacenar novedades del equipo
#se define la clase SistemaGestionEquipos que gestiona la informacion de los equipos

# Se define un diccionario vacio llamado 'equipos' para almacenar la informacion de los equipos de computo.
equipos = {}

# Funcion para agregar un equipo al diccionario 'equipos'
def agregarEquipo(idEquipo, cargador, mouse, ambiente):
    equipos[idEquipo] = EquipoComputo(idEquipo, cargador, mouse, ambiente)
    print("El equipo a sido registrado correctamente")

# Funcion para agregar una novedad a un equipo especifico.
def agregarNovedad(idEquipo, fecha, descripcion):
    if idEquipo in equipos:
        equipos[idEquipo].Novedades.append({'Fecha': fecha, 'Descripcion': descripcion})
        print("La novedad ha sido agregada con exito al equipo con ID {}.".format(idEquipo))
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Funcion para obtener un reporte de equipos con novedades.
def reporteNovedades():
    equiposConNovedades = [equipo for equipo in equipos.values() if equipo.Novedades]
    return equiposConNovedades

# Funcion para mostrar todos los equipos y sus novedades.
def mostrarEquipos():
    for equipo in equipos.values():
        print("ID: {}".format(equipo.ID))
        print("Cargador: {}".format(equipo.Cargador))
        print("Mouse: {}".format(equipo.Mouse))
        print("Ambiente: {}".format(equipo.Ambiente))
        print("Novedades:")
        for novedad in equipo.Novedades:
            print("- Fecha: {}, Descripcion: {}".format(novedad['Fecha'], novedad['Descripcion']))
        print("-------------")

# Funcion para modificar la informacion de un equipo existente.
def modificarEquipo(idEquipo, cargador, mouse, ambiente):
    if idEquipo in equipos:
        equipos[idEquipo].Cargador = cargador
        equipos[idEquipo].Mouse = mouse
        equipos[idEquipo].Ambiente = ambiente
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Funcion para eliminar un equipo del diccionario 'equipos'.
def eliminarEquipo(idEquipo):
    if idEquipo in equipos:
        del equipos[idEquipo]
    else:
        print("El equipo con ID {} no existe.".format(idEquipo))

# Funcion principal que maneja el bucle y las opciones del usuario.
def menu():
    while True:
        print("Opciones de la aplicacion:")
        print("A. Agregar un equipo de computo")
        print("B. Agregar una novedad sobre un equipo")
        print("C. Buscar un equipo por ID")
        print("D. Mostrar reporte de equipos con novedades")
        print("E. Mostrar todos los equipos")
        print("F. Modificar informacion de un equipo")
        print("G. Eliminar un registro de computo")
        print("S. Salir")

        opcion = input("Digite la opcion que desea realizar: ")

        # Se utilizan condicionales para ejecutar la funcion correspondiente segun la opcion ingresada por el usuario.
        if opcion.lower() == 'a':
            # Se solicita la informacion del nuevo equipo y se llama a la funcion 'agregarEquipo'.
            idEquipo = input("Ingrese el ID del equipo que desea agregar: ")
            cargador = input("El equipo cuenta con cargador? (si/no): ")
            mouse = input("El equipo cuenta con mouse? (si/no): ")
            ambiente = input("En que ambiente se encuentra el equipo?: ")
            agregarEquipo(idEquipo, cargador, mouse, ambiente)
        elif opcion.lower() == 'b':
            # Se solicita informacion de la novedad y se llama a la funcion 'agregarNovedad'.
            idEquipo = input("Ingrese el ID del equipo al que le va a registrar una novedad: ")
            fecha = input("Ingrese la fecha de la novedad: ")
            descripcion = input("Ingrese la descripcion de la novedad: ")
            agregarNovedad(idEquipo, fecha, descripcion)
        elif opcion.lower() == 'c':
            # Se busca un equipo por ID y se muestra su informacion si existe.
            idEquipo = input("Ingrese el ID del equipo que desea buscar: ")
            if idEquipo in equipos:
                print("Datos del equipo:")
                print("ID: {}".format(equipos[idEquipo].ID))
                print("Cargador: {}".format(equipos[idEquipo].Cargador))
                print("Mouse: {}".format(equipos[idEquipo].Mouse))
                print("Ambiente: {}".format(equipos[idEquipo].Ambiente))
            else:
                print("El equipo no se encuentra en la base de datos")
        elif opcion.lower() == 'd':
            # Se muestra el reporte de equipos con novedades.
            equiposNovedades = reporteNovedades()
            if not equiposNovedades:
                print("No hay ninguna novedad en los equipos")
            else:
                for equipo in equiposNovedades:
                    print("ID: {}".format(equipo.ID))
                    for novedad in equipo.Novedades:
                        print("- Fecha: {}, Descripcion: {}".format(novedad['Fecha'], novedad['Descripcion']))
        elif opcion.lower() == 'e':
            # Se llama a la funcion para mostrar todos los equipos.
            mostrarEquipos()
        elif opcion.lower() == 'f':
        # Se solicita la informacion para modificar un equipo y se llama
            idEquipo = input("Ingrese el ID del equipo que desea modificar: ")
            cargador = input("El equipo cuenta con cargador? (si/no): ")
            mouse = input("El equipo cuenta con mouse? (si/no): ")
            ambiente = input("En que ambiente se encuentra el equipo?: ")
            modificarEquipo(idEquipo, cargador, mouse, ambiente)
        elif opcion.lower() == 'g':
            # Se solicita el ID del equipo a eliminar y se llama a la funcion 'eliminarEquipo'.
            idEquipo = input("Ingrese el ID del equipo que desea eliminar: ")
            eliminarEquipo(idEquipo)
        elif opcion.lower() == 's':
            # Se sale del bucle si la opcion es 's'.
            break
        else:
            # Se informa al usuario si la opcion ingresada no es valida.
            print("La opcion que ingreso no es valida, verifique las opciones e ingrese una correcta")

    print("El programa ha terminado con exito :D.")

# Se llama a la funcion principal 'menu' para ejecutar el programa.
menu()

