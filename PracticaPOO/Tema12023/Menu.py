from ManejadorFederados import ManejadorFederados
from ManejadorEvaluaciones import ManejadorEvaluaciones
class Menu:
    __options:dict
    __optionsText:list
    __ManejadorFed:ManejadorFederados
    __ManejadorEva:ManejadorEvaluaciones
    def __init__(self):
        self.__options = dict(a=self.option1,b=self.option2,c=self.option3,d=self.option4)
        self.__optionsText = ["a","b","c","d"]
        self.__ManejadorFed = ManejadorFederados()
        self.__ManejadorEva = ManejadorEvaluaciones()
    def option1(self):
        estilo = input("ingrese estilo  buscar")
        edad = input("ingrese edad a buscar")
        evaList = self.__ManejadorEva.buscar(estilo)
        list = self.__ManejadorFed.buscFed(evaList,edad)
        for i in list:
            print(f"patinadores que participaron: \n Apellido: {i.getApellido()} \n Nombre:{i.getNombre()} \n DNI: {i.getDNI()} ")
        self.showMenu()
    def option2(self):
        print("opcion 2")
        self.showMenu()
    def option3(self):
        print("opcion 3")
        self.showMenu()
    def option4(self):
        print("opcion 4")
        self.showMenu()
    def showMenu(self):
        for i in self.__optionsText:
            print(i)
        opcion = input("ingrese opcion(0 para finalizar)")
        fc = self.__options.get(opcion,lambda:print("opcion no existe"))
        fc()
            