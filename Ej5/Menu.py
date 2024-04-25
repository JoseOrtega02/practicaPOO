from Equipo import Equipo
from Fecha import Fecha
from gestorEquipo import gestorEquipo
class Menu:
    def optionA(self):
        id=input("Ingrese identificador del equipo")
        nombre = input("Ingrese nombre del equipo")
        goles = input("Ingrese goles a  favor del equipo")
        golesContra =input("Ingrese goles en contra del equipo")
        diffGoles = input("Ingrese differencia de goles del equipo")
        puntos = input("Ingrese puntos del equipo")
        equipo = Equipo(id,nombre,goles,golesContra,diffGoles,puntos)
        gestorequipo = gestorEquipo()
        gestorequipo.ingresarEquipo(equipo)
        gestorequipo.mostrarEquipo()
    def optionB(self):
        fecha = input("Ingrese la fecha")
        idLocal = input("Ingrese id del equipo local")
        idVisit = input("Ingrese id del equipo Visitante")
        cantGolLocal = input("Ingrese cantidad de goles del equipo local")
        cantGolVisit = input("Ingrese cant de goles del equipo visitante")
        fecha = Fecha(fecha,idLocal,idVisit,cantGolLocal,cantGolVisit)
    def showMenu(self):
        print("a. Leer los datos de los equipos del archivo y almacenarlos en el Gestor de Equipos.")
        print("b. Leer los datos de las Fechas de Fútbol, y almacenarlos en el Gestor de Fechas. ")
        option = input("Ingrese una opcion(0 para finalizar)")
        
        while option != "0":
            if(option == "a"):
                self.optionA()
            elif option == "b":
                self.optionB()
            option = input("Ingrese una opcion(0 para finalizar)")
            