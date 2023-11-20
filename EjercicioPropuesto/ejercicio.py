#Se define una clase llamada equipo que representa un equipo de computo
class Equipo:

    def __init__(self, id_equipo, cargador, mouse, ambiente):
#se inicializa los atributos del equipo
        self.ID = id_equipo
        self.Cargador = cargador
        self.Mouse = mouse
        self.Ambiente = ambiente
        self.Novedades = []#lista para almacenar novedades del equipo
#se define la clase SistemaGestionEquipos que gestiona la informacion de los equipos
class SistemaGestionEquipos:
    def __init__(self):
        self.equipos = {}#se inicializa el  diccionario que almacenara los equipos
#metodo para agregar un nuevo equipo al sistema
    def agregarEquipo(self, idEquipo, cargador, mouse, ambiente):
        self.equipos[idEquipo] = Equipo(idEquipo, cargador, mouse, ambiente)
#metodo para agregar novedades a un equipo existente
    def agregarNovedad(self, idEquipo, fecha, descripcion):
        if idEquipo in self.equipos:
            self.equipos[idEquipo].Novedades.append({'Fecha': fecha, 'Descripcion': descripcion})
            print(f"La novedad ha sido agregada con exito al equipo con ID {idEquipo}")
        else:
            print(f"El equipo con ID {idEquipo} no esta en la base de datos")
#metodo para mostrar equipos con novedades
    def mostrarEquiposConNovedades(self):
        equiposConNovedades = [equipo for equipo in self.equipos.values() if equipo.Novedades]
        return equiposConNovedades#se devuelve la lista de equipos con novedades
#metodo para mostrar todos los equipos y sus novedades
    def mostrarEquipos(self):
        for equipo in self.equipos.values():
            print(f"ID: {equipo.ID}")
            print(f"Cargador: {equipo.Cargador}")
            print(f"Mouse: {equipo.Mouse}")
            print(f"Ambiente: {equipo.Ambiente}")
            print("Novedades:")
            for novedad in equipo.Novedades:
                print(f"- Fecha: {novedad['Fecha']}, Descripcion: {novedad['Descripcion']}")
            print("----------------------")
#metodo para modificar la informacion de un equipo
    def modificarEquipo(self, idEquipo, cargador, mouse, ambiente):
        if idEquipo in self.equipos:
            self.equipos[idEquipo].Cargador = cargador
            self.equipos[idEquipo].Mouse = mouse
            self.equipos[idEquipo].Ambiente = ambiente
        else:
            print(f"El equipo con ID {idEquipo} no existe.")

#metodo para eliminar un equipo del sistema
    def eliminarEquipo(self, idEquipo):
        if idEquipo in self.equipos:
            del self.equipos[idEquipo]
        else:
            print(f"El equipo con ID {idEquipo} no esta en la base de datos.")
#metodo para mostrar el menu de opciones y gestionar las acciones del usuario
    def menu(self):
        while True:
            print("Opciones de la aplicacion:")
            print("A. Agregar un equipo de computo")
            print("B. Agregar una novedad sobre un equipo")
            print("C. Buscar un equipo por ID")
            print("D. Mostrar reporte de equipos con novedades")
            print("E. Mostrar todos los equipos")
            print("F. Modificar información de un equipo")
            print("G. Eliminar un registro de computo")
            print("S. Salir")

            opcion = input("Digite la opcion que desea realizar: ")
#opcion A para agregar un equipo de computo
            if opcion.lower() == 'a':
                idEquipo = input("Ingrese el ID del equipo que desea agregar: ")
                cargador = input("El equipo cuenta con cargador? (si/no): ")
                mouse = input("El equipo cuenta con mouse? (si/no): ")
                ambiente = input("En que ambiente se encuentra el equipo?: ")
                self.agregarEquipo(idEquipo, cargador, mouse, ambiente)
                print(" - El equipo se ha agregado a la bd")
                print("----------------------")

#opcion B para agregar una novedad sobre un equipo
            elif opcion.lower() == 'b':
                idEquipo = input("Ingrese el ID del equipo al que le va a registrar una novedad: ")
                if not self.equipos.get(idEquipo):
                    print("No hay ningun equipo registrado con ese ID. Verifique el ID")
                else:
                    fecha = input("Ingrese la fecha de la novedad: ")
                    descripcion = input("Ingrese la descripcion de la novedad: ")
                    self.agregarNovedad(idEquipo, fecha, descripcion)
                    print("----------------------")

#opcion C para buscar un equipo por ID
            elif opcion.lower() == 'c':
                idEquipo = input("Ingrese el ID del equipo que desea buscar: ")
                if idEquipo in self.equipos:
                    print("Datos del equipo:")
                    print(f"ID: {self.equipos[idEquipo].ID}")
                    print(f"Cargador: {self.equipos[idEquipo].Cargador}")
                    print(f"Mouse: {self.equipos[idEquipo].Mouse}")
                    print(f"Ambiente: {self.equipos[idEquipo].Ambiente}")
                    print("----------------------")
                else:
                    print("El equipo no se encuentra en la base de datos")
                    print("----------------------")
 #opcion D para mostrar reporte de equipos con novedades
            elif opcion.lower() == 'd':
                equiposNovedades = self.mostrarEquiposConNovedades()
                if not equiposNovedades:
                    print("No hay ninguna novedad en los equipos")
                else:
                    for equipo in equiposNovedades:
                        print(f"ID: {equipo.ID}")
                        for novedad in equipo.Novedades:
                            print(f"Fecha: {novedad['Fecha']}")
                            print(f"Descripcion: {novedad['Descripcion']}")
                            print("----------------------")

#opcion E para mostrar todos los equipos          
            elif opcion.lower() == 'e':
                if self.equipos:
                    self.mostrarEquipos()
                else:
                    print("No hay ningun equipo registrado")

#opcion F para modificar informacion de un equipo
            elif opcion.lower() == 'f':
                idEquipo = input("Ingrese el ID del equipo que desea modificar: ")
                cargador = input("El equipo cuenta con cargador? (si/no): ")
                mouse = input("El equipo cuenta con mouse? (si/no): ")
                ambiente = input("En que ambiente se encuentra el equipo?: ")
                self.modificarEquipo(idEquipo, cargador, mouse, ambiente)
                print("----------------------")
#opcion G para eliminar un registro de computo
            elif opcion.lower() == 'g':
                idEquipo = input("Ingrese el ID del equipo que desea eliminar: ")
                print("----------------------")
                self.eliminarEquipo(idEquipo)
#opcion S para salir del bucle y terminar el programa
            elif opcion.lower() == 's':
                break
            else:#mensaje para opciones no validas
                print("La opcion que ingreso no es valida, verifique las opciones e ingrese una correcta")
#mensaje de finalizacion del programa
        print("El programa ha terminado con exito :D.")

# Crear una instancia del sistema de gestion de equipos y ejecutar el menu
sistema = SistemaGestionEquipos()
sistema.menu()


